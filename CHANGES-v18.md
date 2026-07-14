# v18_2026-07-14 — Render-blocking mobil + contrast WCAG

## CONTRAST (Nivel 1 ales)
- `--muted` #8A7060 → #6E5646 (contrast 4.09 → 6.07 pe sand; trece AA)
- `--light` #B09880 → #7E6248 (2.45 → 5.02; trece AA)
- Se propagă automat pe tot site-ul (76 + 8 folosiri). Rezolvă „insufficient contrast ratio".

## RENDER-BLOCKING MOBIL (ținta: cei 1.800 ms)
- **Fonturile Google** scoase de pe calea critică: `media="print" onload="this.media='all'"`
  + `<noscript>` fallback. Textul apare imediat (display=swap), fontul comută după. Toate 12 paginile.
- **Calendly widget.css** scos de pe calea critică (același pattern) pe 11 pagini.
  Popup-ul se declanșează doar la click — CSS-ul e demult încărcat până atunci. (widget.js era deja async.)
- style.css rămâne blocant (e necesar pentru render-ul above-fold).

## CE NU S-A ATINS (și de ce)
- „Forced reflow" — vine din handler-ul de scroll (nav padding), se produce la scroll, NU la încărcare.
  Nu afectează scorul/TBT, doar fluiditatea. Optional de reparat mai târziu (passive listener + prag).
- „Use efficient cache lifetimes ~134 KiB" — sunt scripturi Google (gtag/analytics) servite de pe serverele lor,
  cu cache scurt setat de Google. Nu-l putem controla. Assets-urile noastre (webp/css) au deja cache lung din v17.
- „Legacy JavaScript / Reduce unused JS" — third-party (Calendly/gtag/Meta). Necontrolabil de la noi.

## AȘTEPTĂRI REALISTE
Desktop e deja 93. Pe mobil, testul rulează pe telefon lent + Slow 4G — scorul de laborator e mai sever
decât experiența reală. Scoaterea fonturilor + Calendly de pe calea critică ar trebui să reducă vizibil
render-blocking-ul și să ajute LCP-ul. Re-rulează PageSpeed după deploy.
