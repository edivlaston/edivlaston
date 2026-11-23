# v63 — 2026-11-23 — pagina în engleză (/en) + sursa în formularul de contact

Sursa: `claude-code-pagina-en-2026-11-23.md`.

- `en.html` nou (servit la /en, `/en.html` → /en 301): layout terapie-cuplu, text exact din document, header doar cu logo + WhatsApp + programare, hreflang en/ro/x-default, og:locale en_US, JSON-LD ProfessionalService (`availableLanguage`) + FAQPage (5 întrebări). Ieșiri: Calendly, WhatsApp, /terapie-cuplu.
- index: „Sessions in English →” sub hero; hreflang; `availableLanguage` în JSON-LD. Butonul din hero rămâne la 612px pe 390×664 (cu `?gclid`).
- terapie-cuplu: „Couples therapy in English →” sub primul buton; hreflang (ro spre sine, en spre /en).
- Footer: link `English` pe toate cele 53 de pagini cu footer, inclusiv în șabloanele din `gen-articole.py` / `gen-episoade.py`.
- sitemap.xml + lista din `gen-episoade.py`: /en.
- Formular `contact`: câmpuri ascunse `sursa` și `pagina`. Script inline pe toate paginile: salvează în sessionStorage (`edi_sursa`) gclid/gbraid/wbraid, utm sau referrer/direct, o singură dată pe sesiune; le completează la trimitere. Totul în try/catch.

## De verificat după deploy

- /en live, Rich Results Test (FAQPage), test real de formular cu `?gclid=test` și ștergerea mesajului din Netlify.

## v63b — 2026-11-23 — /en refăcută + EN în meniu

- /en: poză în hero (mare pe desktop, avatar pe telefon), „← Main site (RO)” în header și în footer, secțiuni vizuale (pastile, carduri, servicii alăturate, bandă cu abordarea, 3 pași, carduri de preț). Text comprimat; FAQ și JSON-LD neschimbate.
- Meniu, pe toate paginile cu meniu (și în generatoare): „EN” în meniul desktop, pastilă „EN” lângă hamburger pe mobil, „English” în meniul mobil.
- style.css: stiluri pentru EN; meniul trece în hamburger de la 1290px (înainte 1180px), ca să nu atingă logo-ul.
- `style.css?v=63` pe toate paginile (CSS-ul are cache 7 zile).
