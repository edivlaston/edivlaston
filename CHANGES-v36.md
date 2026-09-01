# v36_2026-09-01 — FAQPage schema pe pagini statice + retragere completă frază v6 + schema note-din-cabinet

## Context

Continuare directă a auditului SEO/AEO din 1 septembrie 2026. Toate modificările de mai jos au fost confirmate explicit de Edi.

## Ce s-a schimbat

1. **FAQPage schema — `barbati.html`** (6 întrebări) și **`terapie-cuplu.html`** (5 întrebări).
   Extrase automat din markup-ul HTML existent (`faq-item`/`faq-q`/`faq-a` pe barbati.html, `<details class="faq-item"><summary>` pe terapie-cuplu.html — cele două pagini folosesc componente FAQ diferite, extragerea a fost adaptată la fiecare). Conținutul vizibil nu s-a schimbat, doar markup-ul structurat a fost adăugat în `<head>`.

2. **Schema ProfessionalService + Person — `note-din-cabinet.html`**.
   Singura din cele 10 pagini principale care nu o avea. Bloc identic cu celelalte 9 pagini.

3. **Articol `de-ce-nu-trece-anxietatea` — restructurare completă:**
   - Toate cele 6 titluri de secțiune convertite din `<h3>` în `<h2>` (structură cerută de `extrage_faq()` din `gen-articole.py`).
   - Secțiunea „Întrebări frecvente" convertită din format prozaic (`<p><strong>Q</strong><br>A</p>`) în formatul `<h2>Întrebări frecvente</h2>` + perechi `<h3>Q</h3><p>A</p>`, cerut de generator.
   - Rezultat: articolul generează acum automat FAQPage schema (5 întrebări) — înainte nu genera nimic, fiind format greșit.
   - **Frază retrasă din BrandVoice v6 eliminată complet**: „Ai înțeles și tot nu s-a schimbat nimic." a fost scoasă din paragraful final și înlocuită cu „Nu ai stricat nimic. Ai ajuns la capătul a ce poate face mintea singură — și de aici încolo se lucrează altfel." — păstrează sensul, elimină exact fraza de pe lista roșie v6 §7. Confirmat cu Edi: retragere completă, fără excepție de hook.
   - Regenerat via `gen-articole.py`.

4. **`sitemap.xml` — `lastmod` actualizat** pentru `/barbati` și `/terapie-cuplu` (paginile modificate azi) la data curentă, în loc de datele înghețate din iunie/iulie. Modificat direct în `gen-episoade.py` (lista `pagini` cu date hardcodate) și regenerat.

## Nerezolvat / rămâne pe listă

- Reclama Google Ads activă cu copy retras — Edi se ocupă direct în interfața Ads.
- Ștergere ad group „Nu reusesc in relatii" + curățare keywords fără trafic — Edi se ocupă.
- Restructurare H2/FAQ pentru celelalte 5 articole fără structură (burnout-la-locul-de-munca, burnout-la-medici, a-fi-tata-dupa-divort, de-ce-faci-tot-bine-si-tot-gresesti, cum-sa-recunosti-ce-simti) — următoarele pe listă, cerute de Edi să fie făcute pe rând.
- `sameAs` pentru Person schema — încă lipsesc URL-urile exacte Hilio/pleso.me/la-psiholog.ro/ROmedic.
- Adresa pe Facebook — verificată live cu screenshot de la Edi: e deja corectă („Maxim Gorki nr 22, parter, ap 2, Bucharest, Romania"). Nota din auditul anterior („Piata Victoriei" pe Facebook) s-a bazat pe un rezultat de căutare Google vechi/necache-uit — nu pe starea live a paginii. Corectat.
