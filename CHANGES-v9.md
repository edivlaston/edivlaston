# v9_2026-04-29 — Privacy Policy GDPR

## Ce s-a schimbat

1. **Pagină nouă:** `confidentialitate.html` — Privacy Policy GDPR-compliant în română
   - Descrie ce date colectez (formular contact, Calendly, Meta Lead Form, GA, Pixel)
   - Bază legală pentru fiecare prelucrare
   - Cu cine partajez datele (Google, Meta, Calendly, Netlify, Hilio)
   - Drepturile persoanelor conform GDPR
   - Confidențialitate profesională (Cod CPR)
   - `<meta name="robots" content="noindex, follow">` — nu apare în Google

2. **Link în footer pe toate paginile:**
   - index.html, barbati.html, adictii.html — în footer-links
   - femei.html, despre.html, contact.html, blog.html, pentru-terapeuti.html — link discret deasupra © (display:block, centered)
   - multumesc.html — neatins (nu are footer)

## ⚠ DE COMPLETAT MANUAL ÎNAINTE DE DEPLOY

În `confidentialitate.html`, secțiunea „1. Cine sunt", înlocuiește placeholder-ele:

- `[ADRESA COMPLETĂ A CABINETULUI]` → strada și numărul exact
- `[CUI-UL CABINETULUI]` → CUI-ul/CIF-ul Cabinetului Individual de Psihologie

Caută în fișier cu Ctrl+F: `[ADRESA` și `[CUI`.

## DUPĂ DEPLOY

În Meta Ads Manager → Lead Form „Evaluare_30min_Barbati" → editează formul → schimbă URL-ul Privacy Policy din:
- `https://calendly.com/privacy`
în:
- `https://edivlaston.ro/confidentialitate`

