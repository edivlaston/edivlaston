# v19_2026-07-14 — Amânare third-party (LCP mobil)

## SCOP: elibera banda pe Slow 4G pentru imaginea LCP
Pe mobil, imaginea (LCP) stătea la coadă după scripturi third-party care se încărcau devreme.
Am amânat cele NEESENȚIALE, fără să ating tracking-ul.

## MODIFICĂRI
- **Calendly** — nu se mai încarcă pe toate paginile la load. Se încarcă la prima interacțiune
  (tap/scroll/tastă) prin `openCal()`. Primul click funcționează instant (helper load-aware).
  `href`-ul spre calendly.com rămâne ca fallback dacă JS pică. 41 CTA-uri, 12 pagini.
- **Ahrefs analytics.js** — amânat după evenimentul `load`. Neesențial, nu blochează critical path.

## NEATINSE (intenționat)
- **gtag (GA + Ads)** și **Meta Pixel** — tracking-ul reparat recent. Amânarea lor ar risca
  pageview-uri și conversii pierdute. Rămân exact cum sunt.

## ⚠ DE TESTAT DUPĂ DEPLOY
Apasă butonul „Rezervă o primă ședință" pe site-ul live — și la primul click (înainte de orice
altă interacțiune) și după. Popup-ul Calendly trebuie să se deschidă normal în ambele cazuri.

## AȘTEPTĂRI
LCP mobil ar trebui să scadă (imaginea prinde banda mai devreme), dar NU va deveni „verde" —
gtag + Meta rămân consumatorii mari de bandă și nu-i atingem. Scorul de laborator pe Slow 4G
oricum nu e semnalul de ranking Google (acela e field data / utilizatori reali).
