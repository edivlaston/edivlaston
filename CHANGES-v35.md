# v35_2026-08-31 — Restaurare AEO (v34) + articol nou „Chiar merită terapia?"

## Context

Un push separat ("reincearca ep 19") a suprascris munca de schema/AEO din v34 — probabil pornit dintr-o copie locală mai veche a repo-ului. Efect: schema ProfessionalService/Person lipsea de pe cele 9 pagini principale, `14.html`/`15.html` (fișiere orfane) reapăruseră, `gen-articole.py` pierduse funcția de extragere automată FAQ. Episodul 19 (Note din Cabinet) a rămas neatins — problema a fost izolată la partea de blog/schema.

## Ce s-a restaurat (din v34)

1. **Schema `ProfessionalService` + `Person`** reinjectată în `<head>` pe toate cele 9 pagini principale (index, despre, barbati, femei, terapie-cuplu, adictii, contact, pentru-terapeuti, intrebari-frecvente) + `blog.html`.
2. **`14.html` / `15.html`** șterse din nou (`git rm`).
3. **`gen-articole.py`** — restaurat `extrage_faq()` + `faq_schema_html()`, funcțional la fiecare rulare.
4. **`intrebari-frecvente.html`** — aliniat `priceRange` la formatul standard („280 lei / ședință", nu „$$").

## Ce s-a adăugat nou

5. **Articol nou** în `articole.json`, primul din listă:
   - id: `chiar-merita-terapia`, categorie: „Despre terapie"
   - conține secțiunea „Formarea din spatele fiecărei ședințe" (3+2+4 ani, 300h terapie proprie, 1000h practică, credite anuale) — text furnizat de Edi.
   - FAQ (5 întrebări) → schema `FAQPage` generată automat.
   - Publicat identic (adaptat) și pe ROmedic, cu linkuri UTM (`romedic/referral/minisite`) către Calendly și edivlaston.ro.
6. **`sitemap.xml`** — adăugată intrarea pentru noul articol.
7. **`blog.html`** — eliminat un bloc mort (`display:none`, invizibil pe site, dar prezent în sursă) „Primele articole apar în curând", cu 2 subiecte duplicate față de articole deja publicate. Eliminată și referința JS aferentă (`getElementById('coming-section')`), care altfel ar fi aruncat o eroare și ar fi blocat randarea grilei de articole.

## Nerezolvat / de urmărit

- Cele 6 articole vechi (import WordPress) tot nu au H2/FAQ.
- `sameAs` pentru Person schema tot lipsește — am nevoie de URL-urile exacte Hilio/pleso.me/la-psiholog.ro/ROmedic.
- **Recomandare de proces:** înainte de orice sesiune nouă de lucru pe cod, un `git pull`/re-clone de pe GitHub previne exact regresia de acum (lucru pornit dintr-o copie locală neactualizată).
