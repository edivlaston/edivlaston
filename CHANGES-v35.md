# v35_2026-08-31 — Articol nou: „Chiar merită terapia?"

Articol MOFU nou adăugat, publicat concomitent și pe ROmedic (secțiunea „Informații pentru pacienți" a minisite-ului Gold).

## Ce s-a implementat

1. **Articol nou în `articole.json`**, adăugat la începutul listei:
   - id: `chiar-merita-terapia`
   - titlu: „Chiar merită terapia? Ce se schimbă, de fapt, după primele ședințe"
   - categorie: „Despre terapie" (categorie nouă, nu exista până acum)
   - conținut structurat cu H2 + secțiune „Întrebări frecvente" în format standard (`<h3>`/`<p>`) — a produs automat 5 întrebări în schema `FAQPage` la rulare `gen-articole.py`.
   - conține paragraf „Formarea din spatele fiecărei ședințe" (3 ani facultate + 2 ani master + 4 ani formare, 300h terapie proprie, 1000h practică, credite anuale) — text furnizat direct de Edi.
   - un link intern către `/despre` (ancora „20 de ani în management corporate").
2. **Regenerat `blog/*.html`** (toate cele 8 pagini) — noul articol devine automat primul în lista „related" pe toate celelalte articole existente.
3. **`sitemap.xml`** — adăugat intrarea pentru `/blog/chiar-merita-terapia`.
4. **Publicat identic (adaptat) și pe ROmedic** — articol propriu în contul Gold, cu link către Calendly și către edivlaston.ro, ambele cu UTM (`utm_source=romedic&utm_medium=referral&utm_campaign=minisite`) pentru atribuire distinctă în GA4.

## Nerezolvat / de urmărit

- Aceleași 6 articole vechi (import WordPress) tot nu au H2/FAQ — nerezolvat, ca și în v34.
- `sameAs` pentru Person schema tot lipsește — încă am nevoie de URL-urile exacte Hilio/pleso.me/la-psiholog.ro/ROmedic.
