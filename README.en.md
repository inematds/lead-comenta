# lead-comenta

[![lead-comenta: comment becomes a guide](guia/assets/banner-en.jpg)](https://inematds.github.io/lead-comenta/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

lead-comenta creates the “free guide” page you promise when you say, “Comment KEYWORD and I’ll send it to you.” It’s for people who post a carousel or reel with this invitation and need the material ready before publishing. You provide the keyword, topic, and a source (a page or text file); it writes a short guide with 4 to 7 steps using only what’s in the source, generates a page in the INEMA format, and prepares texts for replying to the comment, the direct message, and the story. It requires Python 3 and Claude Code; publishing is done through GitHub Pages. Today, the guide page and replies are generated in Portuguese.

## 📖 User guide

Complete guide (landing page + step-by-step): **https://inematds.github.io/lead-comenta/guia/en/**

## Usage

```bash
cd ~/projetos/lead-comenta
python3 lead.py nova AGENTE --tema "6 tarefas chatas que um agente faz" --fonte https://inematds.github.io/empresa-de-ia/guia/
python3 lead.py lista              # words and links
python3 lead.py resposta AGENTE    # ready-to-use reply texts
git add -A && git commit -m "guia AGENTE" && git push   # the page goes live
```

Page: `https://inematds.github.io/lead-comenta/paginas/<palavra>/` · example: [AGENTE](https://inematds.github.io/lead-comenta/paginas/agente/).

## The process, from start to finish

🧠 session with Nei · ⚙️ script · 🤖 `claude -p` (subscription)

| # | Step | Command / what happens | Who |
|---|---|---|---|
| 1 | Keyword + topic | comes from carrossel-inema, r7ex, or Nei | 🧠 |
| 2 | Source | inema.club/project guide page or a .md file with the content | 🧠 |
| 3 | Guide | `lead.py nova PALAVRA --tema … --fonte …` → text from the source only | 🤖 |
| 4 | Page + replies | `paginas/<palavra>/index.html` and `respostas.md`; entry in `palavras.json` | ⚙️ |
| 5 | Publish | `git push` → GitHub Pages | ⚙️ |
| 6 | Reply to commenters | manually with `respostas.md` (for automatic sending, see `DECISAO-DM.md` (in Portuguese)) | 🧠 |

## Limitations

- Does not send messages: see `DECISAO-DM.md` (in Portuguese).
- The guide uses only what’s in the source; a poor source means a short guide.
- Public replies to comments don’t include a link (Instagram tends to hide comments with links).

License: MIT.