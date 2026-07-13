# v16_2026-07-13 — Fix conversie Google Ads

## Problema
Site-ul trimitea conversia spre label-uri INVENTATE care nu existau ca
acțiuni reale în Google Ads → 0 conversii înregistrate, campanii oarbe.

## Ce s-a schimbat (toate cele 12 pagini HTML)

1. **Label real de conversie.** Înlocuit `programare_finalizata` (inventat)
   cu label-ul real generat de Google Ads: `VtMcCPnxyc8cEOLLtuJB`
   (acțiune: "Programare Calendly (web)", Book appointment, Primary).
   Se declanșează pe `calendly.event_scheduled` = programare FINALIZATĂ.

2. **Scos conversia pe click.** Eliminată linia gtag `calendly_click`
   (contoriza click pe link Calendly, nu programare — semnal fals).

## Ce s-a PĂSTRAT (neatins)
- Listener `event_scheduled` (detectarea programării) — funcțional
- `fbq('track','Schedule')` la programare finalizată — Meta
- `fbq('track','Lead')` pe click Calendly — Meta (vezi nota mai jos)
- GA4 event `programare_calendly`, tracking WhatsApp/telefon — neatinse

## Nota pentru mai târziu
`fbq('track','Lead')` pe click e încă activ pe toate paginile. Și el
numără CLICK, nu programare — la fel de imprecis ca fostul calendly_click.
De curățat data viitoare dacă vrei simetrie Meta↔Google.

## Pagini modificate: 12 (toate cu tracking Calendly)
