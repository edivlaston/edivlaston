# v59 — 2026-11-13 — corecturi vizuale

- style.css: meniul desktop rămâne pe un singur rând (înainte se rupea pe două la ~1280px); sub 1180px trece pe hamburger (înainte: sub 680px)
- style.css: contrast footer — linkuri și iconițe `--bark` (7,9:1), copyright `--clay` (4,4:1); înainte 3,0 și 2,2
- style.css: `prefers-reduced-motion` — fără animații pentru cine le-a dezactivat din sistem
- blog + gen-articole.py: cardurile fără imagine nu mai afișează emoji 📖, ci o bandă subțire de culoare
- index, barbati, femei: note cu virgulă („4,9”, „5,0”)
- culoare: butonul de rezervare (`.btn-primary`, `.nav-cta`, `.mobile-cta`) trece de la `--terra` la verde-pin `--pine` #2F4A3F (alb pe buton 9,5:1); pe secțiunile închise folosește #4A7563, ca să nu se piardă în fundal. Verdele e rezervat acestui buton — restul paletei rămâne neschimbat
- barbati: scos override-ul portocaliu de pe butonul de sub testimoniale
