# v37_2026-09-01 — Restructurare articol „Burnout: am rezistat până când n-am mai putut”

## Context

Al doilea articol din lista celor 6 fără H2/FAQ (după `de-ce-nu-trece-anxietatea` în v36). Următorul pe listă, în ordinea de trafic/prioritate din audit.

## Ce s-a schimbat

1. **`burnout-la-locul-de-munca`** — toate cele 8 titluri de secțiune convertite din `<h3>` în `<h2>`.
2. Secțiunea „Întrebări frecvente” restructurată în format `<h2>Întrebări frecvente</h2>` + 4 perechi `<h3>Q</h3><p>A</p>` — generează acum automat FAQPage schema (4 întrebări).
3. Nicio frază de pe lista roșie v6 găsită în articol — nimic de retras aici.
4. Regenerat via `gen-articole.py` + `gen-episoade.py` (sitemap actualizat, 38 URL-uri, fără modificări la structura generală).

## Observație tehnică — nu am atins-o, doar semnalez

Title tag-ul generat pentru acest articol taie cuvântul la mijloc: *„Burnout: am rezistat până când n-am mai pu… · Edi Vlaston”*. Cauza: `gen-articole.py` (linia ~271) trunchiază titlul la 45 de caractere fără să respecte limita de cuvânt, când titlul + sufixul de brand depășesc 60 de caractere. Nu e ceva introdus azi — logica există deja în generator și probabil afectează și alte articole cu titlu lung. Spune-mi dacă vrei să reparăm asta (ex: trunchiere pe ultimul spațiu, nu pe caracter) — e un fix mic în generator, nu în conținut.

## Nerezolvat / rămâne pe listă

- 4 articole încă fără H2/FAQ: burnout-la-medici, a-fi-tata-dupa-divort, de-ce-faci-tot-bine-si-tot-gresesti, cum-sa-recunosti-ce-simti.
- `sameAs` pentru Person schema — încă lipsesc URL-urile exacte.
- Testimoniale reale (Google Business Profile / Hilio) — Edi a decis să lase testimonialele curente neschimbate, nu se mai umblă la ele.
