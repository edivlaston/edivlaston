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
