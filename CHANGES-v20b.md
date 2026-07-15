# v20b_2026-07-15 — Fix abonare Note din Cabinet + titlu EP10

## 1. Abonare (11 pagini + generator)
Problema: codul de trimitere diferea intre fisiere si niciuna din variante nu era sigura.
- `note-din-cabinet.html` + `nc/*.html`: foloseau `URLSearchParams` + `no-cors`.
  Apps Script primea datele in `e.parameter`, dar NU in `e.postData` (JSON).
- `gen-episoade.py`: folosea `Content-Type: application/json` FARA `no-cors`.
  Asta declanseaza preflight CORS, pe care Apps Script nu il suporta -> request esuat.
  Orice episod nou generat pornea deja stricat.

Fix aplicat, identic pe toate cele 11 pagini + generator:
- Datele se trimit SI in query string (`?nume=...&email=...&pagina=...`)
  SI in body ca JSON cu `Content-Type: text/plain;charset=utf-8`.
  Astfel functioneaza indiferent daca Apps Script citeste `e.parameter`
  sau `JSON.parse(e.postData.contents)`.
- `text/plain` e CORS-safelisted -> fara preflight.
- `.then` si `.catch` cheama amandoua `_confirmaAbonare()`, pentru ca
  `mode: 'no-cors'` face raspunsul opac (nu poate fi citit).
- `pagina` corect pe fiecare pagina.

## 2. Titlu EP10 (note-din-cabinet.json)
Titlu EP10 sincronizat: "Două femei locuiesc în Ioana. Și nu se mai suportă." (titlul indexat deja de Google, pastrat).
Conteaza acum: postarea trece pe format SHARE, deci og:title devine titlul de pe cardul Facebook.

## 3. Regenerat
`gen-episoade.py` rulat: 10 pagini in /nc/ + sitemap (24 URL-uri).
EP11 si EP12 (`publicat: false`) corect excluse.

## VERIFICARI
- 11/11 pagini au varianta noua, 0 ramasite din codul vechi
- ID-uri markup <-> JS: modal-nume, modal-email, form-modal-wrap, form-modal-confirmare — toate 1:1
- Functia e in <script> curat, fara src/async
- `node --check` pe JS: OK
- Sitemap: fara EP11/EP12

## DUPA DEPLOY — OBLIGATORIU
Formularul confirma vizual INTOTDEAUNA (limitare `no-cors`).
Singura dovada ca merge: verifica randul nou in Google Sheet dupa un test real.
