# lead-comenta

[![lead-comenta: comentario se convierte en guía](guia/assets/banner-es.jpg)](https://inematds.github.io/lead-comenta/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

lead-comenta crea la página de la «guía gratis» que prometes cuando dices «comenta PALABRA y te la envío». Sirve para quienes publican un carrusel o reel con esa invitación y necesitan tener el material listo antes de publicar. Le das la palabra, el tema y una fuente (una página o un archivo de texto); crea una guía breve de 4 a 7 pasos usando solo lo que aparece en la fuente, genera una página con el formato de INEMA y los textos listos para responder al comentario, al mensaje directo y a la historia. Necesitas Python 3 y Claude Code; la publicación se hace con GitHub Pages. Hoy, la página de la guía y las respuestas se generan en portugués.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/lead-comenta/guia/es/**

## Usar

```bash
cd ~/projetos/lead-comenta
python3 lead.py nova AGENTE --tema "6 tareas molestas que hace un agente" --fonte https://inematds.github.io/empresa-de-ia/guia/
python3 lead.py lista              # palabras y enlaces
python3 lead.py resposta AGENTE    # textos listos para responder
git add -A && git commit -m "guia AGENTE" && git push   # la página se publica
```

Página: `https://inematds.github.io/lead-comenta/paginas/<palavra>/` · ejemplo: [AGENTE](https://inematds.github.io/lead-comenta/paginas/agente/).

## El proceso, de principio a fin

🧠 sesión con Nei · ⚙️ script · 🤖 `claude -p` (suscripción)

| # | Paso | Comando / qué sucede | Quién |
|---|---|---|---|
| 1 | Palabra + tema | viene de carrossel-inema, de r7ex o de Nei | 🧠 |
| 2 | Fuente | página de inema.club/guía del proyecto o archivo .md con el contenido | 🧠 |
| 3 | Guía | `lead.py nova PALAVRA --tema … --fonte …` → texto solo de la fuente | 🤖 |
| 4 | Página + respuestas | `paginas/<palavra>/index.html` y `respostas.md`; registro en `palavras.json` | ⚙️ |
| 5 | Publicar | `git push` → GitHub Pages | ⚙️ |
| 6 | Responder a quien comentó | manualmente con `respostas.md` (envío automático: consulta `DECISAO-DM.md` (en portugués)) | 🧠 |

## Límites

- No envía mensajes: consulta `DECISAO-DM.md` (en portugués).
- La guía se basa solo en lo que aparece en la fuente; una fuente pobre produce una guía breve.
- La respuesta pública al comentario va sin enlace (Instagram tiende a ocultar los comentarios con enlaces).

Licencia: MIT.