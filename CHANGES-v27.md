# v27_2026-07-20 — Fix EP12: pagina lipsa

## Problema
EP12 (Ioana) era publicat:true in JSON — aparea in lista pe /note-din-cabinet,
dar /note-din-cabinet/12 dadea 404. Cauza: dupa schimbarea publicat:true,
NU s-a rulat gen-episoade.py, deci pagina nc/12.html nu exista.
Redirectul cauta un fisier inexistent -> 404.

## Fix
Rulat gen-episoade.py -> nc/12.html generat + sitemap actualizat (28 URL-uri).

## Include si (din versiunile anterioare, pastrate)
- Fix redirect articol anxietate (v26)
- Cuplu in meniu + sitemap + redirect, pret 390 (v25)
