# CHANGES v53 — 2026-09-14

## Note din Cabinet — Episodul 21 publicat pe site

**„Ionuț are 29 de ani. Îl cheamă Ioan."**
- Personaj: Ionuț — rezident ortopedie, prima ședință (arc nou)
- Data episodului: 2026-09-10 (data trimiterii către abonați)
- `publicat: true`
- Disclaimer: varianta lungă, consecventă cu celelalte 20 de episoade

## Fișiere în această arhivă

| Fișier | Ce s-a schimbat |
|---|---|
| `note-din-cabinet.json` | intrare nouă, episodul 21 |
| `note-din-cabinet.html` | EP21 adăugat în secțiunea „Arhivă — Toate episoadele" |
| `nc/21.html` | pagină nouă (generată) |
| `nc/20.html` | regenerată — link „episodul următor" spre 21 |
| `sitemap.xml` | regenerat: 10 pagini + 8 articole + 21 episoade = 39 URL-uri |

## Generatoare rulate
1. `gen-articole.py`
2. `gen-episoade.py`

## De reținut
`gen-episoade.py` NU atinge `note-din-cabinet.html`. Lista din secțiunea „Arhivă" se editează manual la fiecare episod nou — altfel episodul există, dar nu e accesibil din listă și nu e crawlabil de acolo.
