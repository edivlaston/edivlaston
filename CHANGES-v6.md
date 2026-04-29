# v6_2026-04-29 — Meta Pixel integration

## Ce s-a schimbat

1. **Meta Pixel (ID: 1609722646982737)** adăugat în `<head>` pe toate cele 9 pagini HTML, după Google Analytics tags.

2. **Lead event tracking** adăugat înainte de `</body>` pe toate paginile:
   - Captează automat orice click pe orice link care conține `calendly.com`
   - Trimite `fbq('track', 'Lead')` la Meta
   - Trimite și `gtag('event', 'conversion')` la Google Ads (eveniment custom: `calendly_click` — necesită creare în Google Ads ulterior)

3. **multumesc.html** — eveniment Lead suplimentar la page load (cazul când cineva ajunge aici după submit formular contact).

## Pagini modificate (9)

- index.html
- barbati.html
- femei.html
- despre.html
- contact.html
- blog.html
- adictii.html
- pentru-terapeuti.html
- multumesc.html

## Ce NU s-a schimbat

- Conținutul paginilor — niciun text modificat
- Stilul (style.css) — neatins
- Restul scripturilor (Calendly, GA, Ads) — neatinse
- articole.json, sitemap.xml, robots.txt, _redirects — neatinse

## Verificare după deploy

1. Instalează extensia Chrome **Meta Pixel Helper** (link: chrome.google.com/webstore search "Meta Pixel Helper")
2. Intră pe edivlaston.ro
3. Click pe iconița extensiei — trebuie să apară:
   - ✅ Pixel ID: 1609722646982737
   - ✅ PageView event
4. Click pe orice buton "Evaluare 30 min — gratuită"
5. Pe pop-up Calendly, extensia trebuie să arate și:
   - ✅ Lead event
