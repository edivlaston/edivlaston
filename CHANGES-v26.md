# v26_2026-07-20 — Fix link articol anxietate

## Problema
Articolul "de-ce-nu-trece-anxietatea" era in articole.json + fisier .html + sitemap,
dar LIPSEA regula din _redirects care mapeaza URL-ul curat /blog/de-ce-nu-trece-anxietatea
la fisierul .html. Rezultat: cardul aparea pe /blog dar linkul dadea 404.

## Fix
Adaugat in _redirects:
/blog/de-ce-nu-trece-anxietatea   /blog/de-ce-nu-trece-anxietatea.html   200

## Restul
Arhiva clonata proaspat de pe GitHub — include tot ce e live (cuplu in meniu, articol,
/barbati intarit, pret cuplu 390). Nimic suprascris.
