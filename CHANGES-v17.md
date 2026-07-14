# v17_2026-07-14 — Performanță, accesibilitate & fix indexare

## PERFORMANȚĂ (țintă: LCP 12.5s → mult mai jos)
1. **edi-vlaston.webp recomprimat:** 1.219 KB → 69 KB (1000×1245px, quality 80). -94%.
2. **index.html:** `<link rel="preload" as="image" fetchpriority="high">` pentru foto hero
   + pe `<img>`: `fetchpriority="high"`, `decoding="async"`, `width/height` (previne CLS).
3. **preconnect `fonts.gstatic.com`** adăugat pe toate paginile (fonturile veneau de-acolo fără preconnect → render-blocking).
4. **gtag duplicat eliminat** din `<head>` pe 6 pagini (index, barbati, blog, contact, despre, pentru-terapeuti). Blocul `config G-2W226C545N` apărea de 2 ori.
5. **_headers** (nou) — cache lung pentru assets statice (.webp/.svg 30 zile, .css/.js 7 zile). HTML rămâne pe revalidare.

## ACCESIBILITATE (87) + AGENTIC BROWSING (1/2)
6. **aria-label** pe linkurile Facebook/Instagram din footer (index, confidentialitate, note-din-cabinet)
   → rezolvă „Links do not have a discernible name" + „Accessibility tree is not well-formed".
7. **`aria-hidden="true"`** pe SVG-urile decorative (iconițe).
8. **`<main>` landmark** adăugat pe toate paginile de conținut (10) → rezolvă „Document does not have a main landmark". (confidentialitate îl avea deja; multumesc nu are footer, sărită.)

## INDEXARE (din discuția de indexare — soft 404 /edv/services/)
9. **robots.txt:** scos `Disallow: /edv/` (bloca Google să vadă că URL-ul vechi a dispărut).
10. **_redirects:** adăugat `/edv/*  /  301!` → curăță soft 404-ul. Wildcard prinde orice URL vechi `/edv/...`.
    ⚠ ȚINTA e homepage (`/`). Dacă preferi să trimită spre `/barbati`, e o singură modificare — spune.

## RĂMAS DE DECIS (nu inclus — atinge culorile de brand)
- Contrast WCAG: `--muted #8A7060` și `--light #B09880` pe fundal deschis pică pragul. Îți dau separat 2-3 variante de culoare care trec WCAG dar rămân în tonul cald.

## DUPĂ DEPLOY
- Search Console → URL Inspection pe `/edv/services/` → Request indexing (grăbește scoaterea din index).
- Re-rulează PageSpeed pe homepage după ce Netlify termină deploy-ul.
