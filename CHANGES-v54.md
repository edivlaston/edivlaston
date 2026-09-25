# CHANGES v54 — 2026-09-25

## Linkuri interne — de la 1 la 31 de pagini care linkează

Înainte: 9 articole, un singur link articol→articol. 22 de episoade Note din Cabinet, zero linkuri.
După: fiecare episod și fiecare articol din cluster trimit mai departe.

### 1. Linkuri în corpul articolelor (9 inserări)

Ancore naturale în text existent, nu paragrafe adăugate artificial:

| Din | Spre |
|---|---|
| cum-sa-recunosti-ce-simti | suicid-barbati-romania |
| a-fi-tata-dupa-divort | suicid-barbati-romania |
| de-ce-nu-trece-anxietatea | suicid-barbati-romania |
| burnout-la-medici | burnout-la-locul-de-munca, suicid-barbati-romania |
| burnout-la-locul-de-munca | burnout-la-medici |
| suicid-barbati-romania | burnout-la-locul-de-munca, burnout-la-medici, cum-sa-recunosti-ce-simti, chiar-merita-terapia |

### 2. Punte editorială la finalul fiecărui episod (22 episoade)

Un paragraf `<p class="ep-punte">` după disclaimer, mapat pe arcul personajului:

| Personaj | Episoade | Articol |
|---|---|---|
| Mihai | 1–4, 15 | de-ce-faci-tot-bine-si-tot-gresesti |
| Cristina | 5–7 | burnout-la-locul-de-munca |
| Radu | 8, 11 | burnout-la-medici |
| Ioana | 9, 10, 12, 13 | cum-sa-recunosti-ce-simti |
| Bogdan | 14, 16, 17 | chiar-merita-terapia |
| Vlad și Ana | 18–20 | diferenta-de-libido-in-cuplu |
| Ionuț | 21, 22 | suicid-barbati-romania |

Puntea e plasată după disclaimer, ca să nu intre în corpul narativ — episodul se termină la prag, ca întotdeauna.

### 3. Stil nou: `.ep-punte` în gen-episoade.py

Separator sus, corp mai mic, link în terracotta. Se distinge de text ca notă editorială.

## Rezultat

Linkuri interne primite, pe destinație:

- /blog/suicid-barbati-romania — 14
- /blog/chiar-merita-terapia — 12
- /blog/de-ce-faci-tot-bine-si-tot-gresesti — 6
- /blog/cum-sa-recunosti-ce-simti — 5
- /blog/diferenta-de-libido-in-cuplu — 5
- /blog/burnout-la-locul-de-munca — 5
- /blog/burnout-la-medici — 4

## Fișiere în arhivă

`articole.json`, `note-din-cabinet.json`, `gen-episoade.py`, 6 pagini din `blog/`, toate cele 22 din `nc/`, `sitemap.xml` (41 URL-uri).

## Generatoare rulate
1. `gen-articole.py`
2. `gen-episoade.py`
