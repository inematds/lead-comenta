#!/usr/bin/env python3
"""lead-comenta — "comenta PALAVRA que eu te mando o guia": a página do guia grátis e as respostas prontas.

Uso:
  python3 lead.py nova AGENTE --tema "6 tarefas chatas que um agente faz" --fonte https://inematds.github.io/x/guia/
  python3 lead.py nova AGENTE --tema "..." --fonte notas.md --link-final https://inema.club/curso
  python3 lead.py lista                       # palavras já criadas e o link de cada uma
  python3 lead.py resposta AGENTE             # texto pronto para responder o comentário e a mensagem direta

Gera paginas/<palavra>/index.html (página única, sem build) + paginas/<palavra>/respostas.md e registra em palavras.json.
Publicar = git push (GitHub Pages serve https://inematds.github.io/lead-comenta/paginas/<palavra>/).
O texto do guia é escrito pelo claude -p (assinatura) SÓ a partir da fonte dada; nada inventado.
Enviar a mensagem para quem comentou NÃO é feito aqui (ver DECISAO-DM.md).
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
REG = RAIZ / "palavras.json"
BASE_URL = os.environ.get("LEAD_BASE_URL", "https://inematds.github.io/lead-comenta/paginas")


def registro():
    return json.loads(REG.read_text()) if REG.exists() else {}


def ler_fonte(fonte):
    if re.match(r"https?://", fonte):
        bruto = urllib.request.urlopen(urllib.request.Request(fonte, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf8", "ignore")
        bruto = re.sub(r"(?s)<(script|style|nav|footer)[^>]*>.*?</\1>", " ", bruto)
        texto = re.sub(r"<[^>]+>", " ", bruto)
    else:
        texto = Path(fonte).read_text()
    return re.sub(r"\s+", " ", html.unescape(texto)).strip()[:14000]


def escrever_guia(palavra, tema, fonte_txt, link_final):
    pedido = f"""Você escreve guias grátis curtos do INEMA (ensina IA na prática, de graça, para gente comum, sem hype, voz do Nei: "você", frase curta, verbo concreto).
Quem chega aqui comentou "{palavra}" num post sobre: {tema}.
Escreva o guia usando SÓ as informações do material abaixo. Não invente número, ferramenta nem passo. Se faltar algo, deixe de fora.
Devolva APENAS um JSON:
{{"titulo": "até 60 caracteres", "subtitulo": "1 frase com a promessa", "para_quem": "1 frase",
 "passos": [{{"titulo": "verbo no imperativo, até 50 caracteres", "texto": "2 a 3 frases", "comando": "comando ou texto para copiar, ou vazio"}}],
 "cuidado": "1 frase com o principal cuidado", "proximo": "1 frase chamando para o material completo"}}
Entre 4 e 7 passos.

MATERIAL:
{fonte_txt}
"""
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}  # assinatura, nunca API
    env["PATH"] = f"{Path.home()}/.local/bin:{Path.home()}/.npm-global/bin:" + env.get("PATH", "")
    out = subprocess.run(["claude", "-p", "--allowedTools", ""], input=pedido, capture_output=True, text=True, timeout=600, env=env).stdout
    m = re.search(r"\{.*\}", out, re.S)
    if not m:
        sys.exit("o claude -p não devolveu o JSON do guia:\n" + out[-800:])
    g = json.loads(m.group(0))
    g["link_final"] = link_final
    return g


def pagina(palavra, g):
    e = html.escape
    passos = "".join(
        f'<li><h3>{e(p["titulo"])}</h3><p>{e(p["texto"])}</p>'
        + (f'<pre><code>{e(p["comando"])}</code><button class="cp" type="button">copiar</button></pre>' if p.get("comando") else "")
        + "</li>" for p in g["passos"])
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(g['titulo'])} — guia grátis INEMA</title><meta name="description" content="{e(g['subtitulo'])}">
<style>
@font-face{{font-family:Sora;font-weight:100 800;src:url(../../assets/Sora.ttf)}}
:root{{--bg:#0c0c10;--card:#15151c;--line:#2a2a35;--ink:#f5f5f7;--mut:#aab4c3;--brand:#FACC15;--brand-ink:#1a1206}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Inter,system-ui,sans-serif}}
main{{max-width:760px;margin:0 auto;padding:36px 20px 60px}}.tag{{display:inline-block;background:var(--brand);color:var(--brand-ink);font:800 .8rem Sora,sans-serif;letter-spacing:.08em;padding:.35em .8em;border-radius:999px}}
h1{{font:800 clamp(1.9rem,6vw,2.7rem)/1.1 Sora,sans-serif;margin:16px 0 8px}}.sub{{color:var(--mut);font-size:1.1rem;margin:0 0 6px}}.para{{color:var(--mut);font-size:.95rem}}
ol{{list-style:none;counter-reset:p;padding:0;margin:28px 0}}ol li{{counter-increment:p;position:relative;border:1px solid var(--line);background:var(--card);border-radius:14px;padding:18px 18px 16px 64px;margin:12px 0}}
ol li::before{{content:counter(p);position:absolute;left:18px;top:16px;font:800 1.6rem Sora,sans-serif;color:var(--brand)}}h3{{font:700 1.1rem Sora,sans-serif;margin:0 0 6px}}ol p{{margin:0}}
pre{{position:relative;background:#000;border:1px solid var(--line);border-radius:12px;padding:12px 70px 12px 12px;overflow:auto;margin:10px 0 0;font:14px/1.5 ui-monospace,monospace}}
.cp{{position:absolute;right:8px;top:8px;background:var(--brand);color:var(--brand-ink);border:0;border-radius:8px;font:700 .75rem Sora,sans-serif;padding:.4em .7em;cursor:pointer}}
.cuidado{{border-left:4px solid var(--brand);background:var(--card);padding:12px 16px;border-radius:0 12px 12px 0}}
.cta{{display:inline-block;margin-top:22px;background:var(--brand);color:var(--brand-ink);font:800 1rem Sora,sans-serif;padding:.9em 1.4em;border-radius:10px;text-decoration:none}}
footer{{margin-top:40px;color:var(--mut);font-size:.85rem}}a{{color:var(--brand)}}
</style></head><body><main>
<span class="tag">GUIA GRÁTIS · {e(palavra)}</span>
<h1>{e(g['titulo'])}</h1><p class="sub">{e(g['subtitulo'])}</p><p class="para">{e(g['para_quem'])}</p>
<ol>{passos}</ol>
<p class="cuidado"><b>Cuidado:</b> {e(g['cuidado'])}</p>
<p>{e(g['proximo'])}</p>
{f'<a class="cta" href="{e(g["link_final"])}">Ver o material completo</a>' if g.get('link_final') else ''}
<footer>INEMA.CLUB · IA na prática, de graça · <a href="https://inema.club">inema.club</a></footer>
</main><script>
document.querySelectorAll('.cp').forEach(b=>b.addEventListener('click',()=>{{navigator.clipboard.writeText(b.previousElementSibling.textContent);b.textContent='copiado';setTimeout(()=>b.textContent='copiar',1500)}}));
</script></body></html>
"""


def respostas(palavra, g, url):
    return f"""# Respostas prontas — {palavra}

Link do guia: {url}

## Resposta pública no comentário (curta, sem link: o Instagram esconde comentário com link)
Te mandei no direct! Se não chegar, me chama por lá com {palavra}.

## Mensagem direta (DM)
Oi! Aqui está o guia grátis que você pediu: **{g['titulo']}**
{url}
São {len(g['passos'])} passos curtos. Qualquer dúvida, responde aqui.

## Story (texto)
Quem comentou {palavra}: o guia já está no seu direct. Ainda não comentou? Vai no post e comenta {palavra}.
"""


def cmd_nova(a):
    palavra = a.palavra.strip().upper()
    if not re.fullmatch(r"[A-ZÀ-Ú0-9]{3,14}", palavra):
        sys.exit("palavra: uma palavra só, 3 a 14 letras")
    reg = registro()
    if palavra in reg and not a.refaz:
        sys.exit(f"{palavra} já existe ({reg[palavra]['url']}); use --refaz para gerar de novo")
    print("lendo a fonte…", flush=True)
    fonte_txt = ler_fonte(a.fonte)
    print("escrevendo o guia (claude -p)…", flush=True)
    g = escrever_guia(palavra, a.tema, fonte_txt, a.link_final or (a.fonte if a.fonte.startswith("http") else ""))
    slug = palavra.lower()
    pasta = RAIZ / "paginas" / slug
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / "index.html").write_text(pagina(palavra, g))
    (pasta / "guia.json").write_text(json.dumps(g, ensure_ascii=False, indent=2))
    url = f"{BASE_URL}/{slug}/"
    (pasta / "respostas.md").write_text(respostas(palavra, g, url))
    reg[palavra] = {"url": url, "tema": a.tema, "fonte": a.fonte, "criado": date.today().isoformat()}
    REG.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n")
    print(f"pronto: {pasta}/index.html\nlink depois do push: {url}\nrespostas: {pasta}/respostas.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("nova")
    n.add_argument("palavra")
    n.add_argument("--tema", required=True)
    n.add_argument("--fonte", required=True, help="URL ou arquivo .md/.txt com o conteúdo do guia")
    n.add_argument("--link-final", default="", help="link do material completo (padrão: a fonte, se for URL)")
    n.add_argument("--refaz", action="store_true")
    sub.add_parser("lista")
    r = sub.add_parser("resposta")
    r.add_argument("palavra")
    a = ap.parse_args()
    if a.cmd == "nova":
        cmd_nova(a)
    elif a.cmd == "lista":
        for k, v in registro().items():
            print(f"{k:14} {v['criado']}  {v['url']}  ({v['tema']})")
    else:
        p = RAIZ / "paginas" / a.palavra.lower() / "respostas.md"
        print(p.read_text() if p.exists() else f"{a.palavra} não existe")


if __name__ == "__main__":
    main()
