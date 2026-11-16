# v62 — 2026-11-16 — pagini de destinație pentru Google Ads

Sursa: `modificari-site-ads-2026-11-16.md` (date Ads 2–15 nov). Commit `e8fff7f`.

- index, hero: rândul de deasupra H1 devine „Psiholog și psihoterapeut · Sector 1, București · și online”; sub nume, „Psiholog · psihoterapeut acreditat · cod 22334”. H1 neschimbat.
- index, hero: al doilea paragraf din `hero-lead` mutat sub `hero-note`; `.hero-lead` margin-bottom 40px → 28px (butonul de rezervare urcă deasupra pliului pe telefon)
- index, hero: `hero-note` arată adresa: „50 de minute · Str. Maxim Gorki 22, Sector 1 (Primăverii) · sau online”
- index, hero: scoase `opacity:0` + `animation` de pe `.hero-tag`, `h1`, `.hero-lead`, `.hero-actions`, `.hero-note`, `.hero-right`, `.hero-mini` și de pe paragraful cu calendarul. `@keyframes` și `.reveal` neatinse.
- index + barbati: pastila „Noiembrie · Tu cu cine vorbești?” se ascunde și pentru traficul din reclame (`gclid`, `gbraid`, `wbraid`, `utm_medium=cpc`); dispare oricum de la 1 decembrie
- terapie-cuplu: întrebare nouă în FAQ, „Ne gândim la divorț. Mai are rost terapia de cuplu?” (pagină + schema FAQPage, 6 întrebări)
- „Primăverii” doar lângă adresă, în tot repo-ul:
  - meta/og/twitter: index („Psiholog și psihoterapeut în București, Sector 1, și online.”), barbati, femei, contact, terapie-cuplu
  - terapie-cuplu: hero „cabinetul din Sector 1, pe strada Maxim Gorki”; „la cabinetul din Sector 1”
  - barbati (FAQ + schema), cu-cine-vorbesti, ghid-anxietate, preturi, intrebari-frecvente (despre terapeut): „Sector 1” / „Sector 1, București”
  - despre: eticheta „Psihoterapeut · Primăverii” → „Psihoterapeut · Sector 1, București”
  - intrebari-frecvente (pagină + schema) și femei: „Str. Maxim Gorki 22, Sector 1 (Primăverii)”
  - articole.json + blog/burnout-la-locul-de-munca, burnout-la-medici, de-ce-nu-trece-anxietatea: „la cabinet în Sector 1 sau online”
  - llms.txt: descrierea și rândul de terapie de cuplu
  - rămase ca atare (deja lângă stradă): contact, despre, confidentialitate, terapie-cuplu, llms.txt

## Verificat live (390×664, fonturi reale)

- cu `?gclid=test`: butonul „Rezervă o primă ședință” se termină la 612px; pastila nu apare
- fără parametru: pastila apare, butonul se termină la 742px (sub pliu până la 1 decembrie)
- titlul și butonul din hero vizibile imediat
- JSON-LD FAQPage de pe /terapie-cuplu se parsează, 6 întrebări. Rich Results Test nerulat.

## Rămas în contul Google Ads (nu în repo)

Pașii A–I din document. „consiliere divort” poate rămâne activ, FAQ-ul e live.
