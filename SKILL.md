---
name: lead-comenta
description: Página do "guia grátis" para o convite "comenta PALAVRA" — a partir da palavra, do tema e de uma fonte (página ou .md), escreve um guia de 4–7 passos só com o que está na fonte, gera a página INEMA (GitHub Pages) e os textos prontos para comentário, DM e story. Gatilho: "comenta X", "página do guia grátis", "lead por comentário", "palavra do carrossel".
---

# lead-comenta

```bash
cd ~/projetos/lead-comenta
python3 lead.py nova PALAVRA --tema "<tema do post>" --fonte <URL ou arquivo .md> [--link-final <material completo>]
```

1. Antes de gerar, confira que a fonte abre e trata do tema (de preferência a página do inema.club/guia do projeto).
2. Leia a página gerada (`paginas/<palavra>/index.html`) e o `guia.json`: nenhum passo pode trazer dado que não esteja na fonte.
3. Mostre ao Nei; com o OK, `git push` (autor inematds). A página vai ao ar em ~1 min.
4. Entregue o link e o `respostas.md`. Enviar DM não é automático (ver `DECISAO-DM.md`).
