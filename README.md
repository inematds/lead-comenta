# lead-comenta

## O que é

O lead-comenta cria a página do "guia grátis" que você promete quando diz "comenta PALAVRA que eu te mando". Serve para quem posta carrossel ou reel com esse convite e precisa ter o material pronto antes de publicar. Você dá a palavra, o tema e uma fonte (uma página ou um arquivo de texto); ele escreve um guia curto de 4 a 7 passos só com o que está na fonte, gera uma página no padrão INEMA e os textos prontos para responder o comentário, a mensagem direta e o story. Precisa de Python 3 e do Claude Code; a publicação é pelo GitHub Pages.

## Usar

```bash
cd ~/projetos/lead-comenta
python3 lead.py nova AGENTE --tema "6 tarefas chatas que um agente faz" --fonte https://inematds.github.io/empresa-de-ia/guia/
python3 lead.py lista              # palavras e links
python3 lead.py resposta AGENTE    # textos prontos para responder
git add -A && git commit -m "guia AGENTE" && git push   # a página vai ao ar
```

Página: `https://inematds.github.io/lead-comenta/paginas/<palavra>/` · exemplo: [AGENTE](https://inematds.github.io/lead-comenta/paginas/agente/).

## O processo, do início ao fim

🧠 sessão com o Nei · ⚙️ script · 🤖 `claude -p` (assinatura)

| # | Passo | Comando / o que acontece | Quem |
|---|---|---|---|
| 1 | Palavra + tema | vem do carrossel-inema, do r7ex ou do Nei | 🧠 |
| 2 | Fonte | página do inema.club/guia do projeto ou arquivo .md com o conteúdo | 🧠 |
| 3 | Guia | `lead.py nova PALAVRA --tema … --fonte …` → texto só da fonte | 🤖 |
| 4 | Página + respostas | `paginas/<palavra>/index.html` e `respostas.md`; registro em `palavras.json` | ⚙️ |
| 5 | Publicar | `git push` → GitHub Pages | ⚙️ |
| 6 | Responder quem comentou | à mão com `respostas.md` (envio automático: ver `DECISAO-DM.md`) | 🧠 |

## Limites

- Não envia mensagens: ver `DECISAO-DM.md`.
- O guia sai só do que está na fonte; fonte pobre = guia curto.
- Resposta pública no comentário vai sem link (o Instagram tende a esconder comentário com link).

Licença: MIT.
