# v22_2026-07-18 — Renumerotare EP11/EP12 + publicare Radu

## Renumerotare (swap)
Motiv: episodul cu Radu (criza din spital) fusese trimis unui abonat pe 10 iulie
ca "episod nou". Devine oficial EP11 si se publica azi. Episodul cu Ioana (decizia)
trece pe pozitia 12 si se publica luni 20 iulie.

- EP11 ACUM = Radu, "O pierdere. Nu te poti opri." — subtitlu "Episodul 11 — Radu, a doua intalnire"
  publicat: true, data 2026-07-18
- EP12 ACUM = Ioana, "Ioana nu mai cere voie ca sa existe" — subtitlu "Episodul 12 — Ioana, saptamana a treia"
  publicat: false, data 2026-07-20 (se publica luni)

## Regenerat
gen-episoade.py: 11 pagini in /nc/ + sitemap (25 URL-uri).
EP12 (publicat:false) corect exclus din /nc/ generat si din sitemap.
Pagina-index note-din-cabinet.html citeste JSON live si filtreaza publicat!==false —
EP11 apare automat, EP12 ascuns automat. Fara editare manuala.

## Verificari
- nc/11.html title/og = Radu ("O pierdere. Nu te poti opri.")
- sitemap: /note-din-cabinet/11 prezent, /12 absent
- abonare intacta pe nc/11 (2 aparitii _confirmaAbonare, 0 cod vechi)

## De facut luni 20 iulie
Publicare EP12 Ioana: schimba publicat:true in JSON, ruleaza gen-episoade.py, re-deploy.
