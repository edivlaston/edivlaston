# v31_2026-07-28 — Articol nou pe blog: burnout (poveste personală)

## „Burnout: am rezistat până când n-am mai putut"

Articol pe clusterul de achiziție **burnout** (§8), poartă personală: momentul demisiei
după o perioadă lungă de presiune pe rezultate. Dezvoltat cu idei din trei surse
(Lucy Brazier — designul muncii; Hobbs — burnout ca semnal contextual; de Vries —
epuizare vs. burnout), toate reformulate în cadru NEACUZATOR.

- **id / URL:** `/blog/burnout-la-locul-de-munca`
- **Categorie:** Burnout (existentă)
- **Keyword principal:** burnout la locul de muncă
- **Frame-ul central (validat cu Edi):** presiunea NU e greșeala nimănui — parte din
  viața unei companii. Critica se mută de pe „organizația se eschivează" pe „avem un
  singur răspuns la presiune și mereu îl dăm spre om". Zero învinuire a managerilor
  (care sunt ei înșiși ICP).
- **A treia opțiune:** între „rezistă mai mult" și „pleacă" — să te oprești și să auzi
  ce-ți cere epuizarea. Edi n-a avut-o; o ține acum pentru alții.
- ~1.408 cuvinte corp. Fără emoji, fără AI-isms, fără promisiuni, fără „gratuit".
- Adresă: Primăverii. Zero fraze retrase v6. Fără sloganul „20 de ani în management".

## Fișiere modificate
- `articole.json` — articol nou, primul în listă
- `blog.html` — card fallback (no-JS) adăugat sus în grid
- `blog/burnout-la-locul-de-munca.html` — pagină generată nouă
- `blog/*.html` — toate regenerate („Citește mai departe" include noul articol)
- `sitemap.xml` — URL nou + `/blog` lastmod → 2026-07-28

## Notă de consistență (de decis de Edi)
Articolul e o poveste publică de reconversie-după-clacare. BrandVoice v6 (implementat în
v30) a mutat POZIȚIONAREA departe de acest cadru. Aici e tratat ca CONȚINUT/narativ
(cum a rămas și articolul de anxietate cu teza lui), nu ca poziționare: nu apare
sloganul „20 de ani în management", iar reconversia e spusă sec, nu ca triumf. Dacă Edi
preferă să nu aibă public povestea de clacare, articolul se poate depersonaliza.

## Însoțit de
- Post LinkedIn (personal, scurt, link în primul comentariu spre acest articol) — livrat în chat.

## Deploy
1. Copiază conținutul arhivei peste repo.
2. `git add -A && git commit && git push` (Netlify deploy automat).
   NU rula din nou gen-articole.py dacă nu editezi articole.json.
