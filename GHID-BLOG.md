# Cum adaugi un articol nou pe blog

## Structura fișierelor pe GitHub

```
site/
├── articole.json        ← EDITEZI DOAR ACESTA
├── imagini/             ← ÎNCARCI IMAGINILE AICI
│   ├── articol-001.jpg
│   ├── articol-002.jpg
│   └── ...
├── blog.html
├── index.html
└── ...
```

---

## Pasul 1 — Scrii articolul în Google Docs

Scrie articolul normal. Când ești mulțumit, copiază tot textul.

**Format recomandat:**
- Paragrafe scurte, separate printr-un rând gol
- Fără titluri de secțiune (h2, h3) — doar text curgător
- Maxim 600–900 cuvinte

---

## Pasul 2 — Încarci imaginea pe GitHub

1. Mergi pe GitHub, în repository-ul site-ului tău
2. Intră în folderul `imagini/`
3. Click **Add file → Upload files**
4. Drag & drop imaginea (format JPG sau WebP, minim 1200x675px)
5. Numește-o clar: `articol-003.jpg` (numărul următor în ordine)
6. Click **Commit changes**

---

## Pasul 3 — Editezi `articole.json`

1. Pe GitHub, deschide fișierul `articole.json`
2. Click pe **pictograma creion** (Edit this file)
3. Adaugă articolul nou la **începutul listei** (după prima `[`)

### Structura unui articol

```json
{
  "id": "003",
  "titlu": "Titlul articolului tău",
  "categorie": "Relații & Bărbați",
  "data": "2026-05-01",
  "imagine": "imagini/articol-003.jpg",
  "rezumat": "1-2 propoziții care apar pe card. Trebuie să atragă atenția.",
  "continut": "Primul paragraf al articolului.\n\nAl doilea paragraf. Separă paragrafele cu \\n\\n exact așa.\n\nAl treilea paragraf. Și tot așa."
}
```

### Categorii disponibile

- `Relații & Bărbați`
- `Psihologie masculină`
- `Povești terapeutice`
- `Reflecții`

---

## Pasul 4 — Salvezi pe GitHub

1. Verifică că JSON-ul e corect (fiecare articol între `{ }`, separate prin `,`)
2. Click **Commit changes**
3. Netlify face deploy automat în 1-2 minute
4. Articolul apare pe site

---

## Exemplu complet — articole.json cu 3 articole

```json
[
  {
    "id": "003",
    "titlu": "Articolul cel mai nou",
    "categorie": "Relații & Bărbați",
    "data": "2026-05-01",
    "imagine": "imagini/articol-003.jpg",
    "rezumat": "Rezumat scurt care apare pe card.",
    "continut": "Primul paragraf.\n\nAl doilea paragraf.\n\nAl treilea paragraf."
  },
  {
    "id": "002",
    "titlu": "Al doilea articol",
    "categorie": "Psihologie masculină",
    "data": "2026-04-15",
    "imagine": "imagini/articol-002.jpg",
    "rezumat": "Rezumat articol 2.",
    "continut": "Conținut articol 2.\n\nParagraful 2."
  },
  {
    "id": "001",
    "titlu": "Primul articol",
    "categorie": "Relații & Bărbați",
    "data": "2026-04-11",
    "imagine": "imagini/articol-001.jpg",
    "rezumat": "Rezumat articol 1.",
    "continut": "Conținut articol 1.\n\nParagraful 2."
  }
]
```

---

## Atenție — greșeli frecvente

❌ **Ghilimele duble în conținut** — dacă textul conține `"` înlocuiește cu `'`

❌ **Lipsă virgulă** între articole — fiecare articol (în afară de ultimul) trebuie urmat de `,`

❌ **Data în format greșit** — folosește întotdeauna `YYYY-MM-DD` (ex: `2026-05-01`)

---

## Dacă nu ai imagine

Poți lăsa câmpul `imagine` gol sau îl ștergi complet:

```json
"imagine": ""
```

Pe card va apărea un placeholder cu emoji 📝.

---

## Verificare rapidă a JSON-ului

Înainte să dai commit, copiază tot conținutul fișierului și lipește-l pe:
**https://jsonlint.com** → click Validate JSON

Dacă e verde — e corect. Dacă e roșu — caută eroarea indicată.
