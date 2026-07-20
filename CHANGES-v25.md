# v25_2026-07-20 — Consolidare: cuplu în meniu + articol anxietate + /barbati întărit

## Context
v23 (cuplu) era live pe GitHub. v24 (articol anxietate) fusese făcut într-o discuție
paralelă, pe un repo FĂRĂ cuplu — deci nu putea fi urcat direct (ar fi șters cuplu).
v25 consolidează totul pe clona reală de pe GitHub: cuplu + articol + îmbunătățiri, o
singură arhivă, fără suprascrieri.

## 1. Terapie de cuplu ÎN MENIU
Până acum /terapie-cuplu era doar landing (fără link în nav). Acum apare în meniul
principal (desktop + mobil) pe toate paginile, lângă „Pentru Ele".
- Adăugat în 29 pagini HTML + în gen-episoade.py (template) → episoadele viitoare îl includ automat.
- Adăugat și în lista de pagini statice din gen-episoade.py (sitemap) — nu mai dispare la regenerare.

## 2. Articol nou pe blog: „De ce nu trece anxietatea, deși ai înțeles-o"
Preluat integral din v24 (text aprobat de Edi, needeployat până acum).
- id/URL: /blog/de-ce-nu-trece-anxietatea · categorie Anxietate
- Miez: insight ≠ schimbare; înțelegerea ca evitare (Segment D). Gendlin + Borkovec.
- Fraza de brand v6: „Înțelegerea îți spune unde ești. Nu te și mută."
- Adresă corectată la Primăverii (era Primăverii deja în v24 — ok).

## 3. Pagina /barbati întărită cu miezul articolului
- Pull-quote actualizat la fraza de brand nouă („Înțelegerea îți spune unde ești. Nu te și mută.")
  + metafora hărții (cea mai puternică imagine din articol).
- Link intern nou din secțiunea „Realitatea" → /blog/de-ce-nu-trece-anxietatea
  (bun pentru SEO + pentru cine vrea mai mult).

## 4. Fix adrese vechi găsite la verificare (bonus)
- blog/burnout-la-medici.html + articole.json: „Piața Victoriei" → „Primăverii" (articol vechi scăpat la migrare).
- confidentialitate.html: placeholder „[Calea Victoriei nr 155...]" → adresa reală Maxim Gorki 22.
  (Document legal — conta.)

## Verificat
- Cuplu în meniu pe toate paginile ✓ · pagina + preț 390 lei ✓ · în sitemap ✓
- Articol anxietate: pagină + card blog + sitemap ✓
- /barbati: fraza nouă + link intern ✓
- ZERO „Victoriei" pe tot site-ul (Piața și Calea) ✓
- Sitemap: 27 URL-uri (11 pagini + 5 articole + 11 episoade)
- EP12 (Ioana) rămâne publicat:false — se publică separat după avansul la abonați

## De făcut de Edi
- Deploy: copiază peste repo, git add -A && commit && push.
- Decizia Calendly pentru cuplu (formular contact vs link generic) — încă deschisă, nu blochează deploy-ul.
