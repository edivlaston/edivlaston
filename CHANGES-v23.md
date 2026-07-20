# v23_2026-07-19 — Pagina noua /terapie-cuplu

## Ce s-a adaugat
Pagina noua terapie-cuplu.html — spoke pe cererea reala de cautare "consiliere cuplu"
(~4.800 afisari/luna, singurul termen care a convertit vreodata in contul Google Ads).

Pozitionare: cuplu INCLUS (nu pivot). "In doi sau singur — cum alegi formatul."
Ofera ambele usi: sedinta de cuplu 80 min / individual 50 min. Triaj clinic, nu redirectare.

Structura (template identic cu femei.html — Cormorant+Jost, paleta calda):
- Hero: "Cauti consiliere de cuplu. Uneori pasul dinaintea ei e altul."
- 3 carduri situatie (aceleasi certuri / tacere / cineva a spus-o)
- "In doi sau singur" — cum alegi formatul
- "Nu tin partea nimanui" — cum lucrez
- 5 FAQ (SEO featured snippets)
- CTA band: 420 lei cuplu / 280 lei individual + Calendly

## Tehnic
- Pret sedinta cuplu: 420 lei / 80 min (PROPUS — de confirmat de Edi)
- Slug: /terapie-cuplu (redirect .html->clean adaugat in _redirects)
- sitemap.xml: intrare noua, priority 0.9
- Tracking intact: GA4 programare_calendly + Google Ads conversion VtMcCPnxyc8cEOLLtuJB
  + Meta Pixel Schedule. Aceleasi ca pe restul site-ului.
- NU e in nav principal (e pagina spoke/landing — ajunge din Google Ads + sitemap + cautare)
- Adresa: Maxim Gorki 22 (corect, post-migrare)

## DE CONFIRMAT de Edi inainte sau dupa deploy
1. Pretul 420 lei — daca schimba, e in 2 locuri: CTA band <p> si FAQ "Cat dureaza".
2. Eveniment Calendly "Sedinta de cuplu 80 min" — momentan link-ul Calendly e cel generic
   (eduard-vlaston-eiv3). Daca creeaza tip de eveniment separat pentru cuplu, se schimba href-ul.

## Google Ads (de facut de Edi, separat de deploy)
Ad group nou, Final URL /terapie-cuplu, Phrase+Exact pe: consiliere cuplu, terapeut de cuplu,
terapie de cuplu, probleme in relatie, consiliere divort. Vezi checklist separat.
