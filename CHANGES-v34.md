# v34_2026-08-28 — AEO: schema pe pagini principale, FAQPage auto, llms.txt, curățare

Audit + implementare pentru optimizare AEO (citare de către AI/LLM-uri: ChatGPT, Claude, Perplexity, Google AI Overview), pornit de la constatarea că homepage, despre, servicii nu aveau deloc schema structurată, deși erau exact paginile care definesc entitatea „Edi Vlaston" pentru un motor de răspuns.

## Ce s-a găsit la audit

- **Zero schema JSON-LD** pe `index.html`, `despre.html`, `barbati.html`, `femei.html`, `terapie-cuplu.html`, `adictii.html`, `contact.html`, `pentru-terapeuti.html`, `blog.html`.
- Articolele de blog aveau schema `Article` dar **fără `FAQPage`**, deși conțin secțiune „Întrebări frecvente" scrisă (`<h2>` + perechi `<h3>/<p>`) — conținut existent, marcaj lipsă.
- `14.html` și `15.html` existau **la rădăcina site-ului** (deployate live pe `edivlaston.ro/14.html` și `/15.html`), aproape identice cu `nc/14.html` și `nc/15.html` — conținut duplicat orfan, tracked în git, probabil rămas dintr-o rulare greșită de generator. Nu erau în sitemap, dar erau accesibile.
- Doar 1 din 7 articole de blog (`diferenta-de-libido-in-cuplu`, cel mai recent) respectă structura standard cu H2-uri; celelalte 6 (import WordPress mai vechi) nu au niciun `<h2>` — folosesc doar `<h3>` fără secțiune FAQ dedicată. **Nerezolvat în acest pas** — e muncă de restructurare conținut, nu de tehnic/schema; necesită trecere prin skill-ul de rescriere articole (04).
- Niciun link vizibil pe site către profilele externe (Hilio, pleso.me, la-psiholog.ro, ROmedic) — doar mențiune text "Hilio.ro" fără link. Blochează construirea unui `sameAs` real în schema `Person`. **Nerezolvat — am nevoie de URL-urile exacte de la Edi.**

## Ce s-a implementat

1. **Schema `ProfessionalService` + `Person`** injectată în `<head>` pe toate cele 9 pagini de mai sus — nume, adresă, telefon, email, preț, acreditare CPR 22334, link spre `/despre`. Format identic cu blocul deja validat pe `intrebari-frecvente.html`.
2. **`gen-articole.py`** — funcție nouă `extrage_faq()` care parsează automat secțiunea „Întrebări frecvente" din `continut` (perechi `<h3>/<p>`) și generează schema `FAQPage` corespunzătoare, injectată automat la fiecare rulare a generatorului. Nu necesită intervenție manuală — funcționează pentru orice articol viitor care respectă structura standard din skill 04.
3. **`llms.txt`** nou la rădăcină — rezumat al brandului, linkuri către paginile-cheie, informații practice. Standard neconfirmat de crawlerele AI majore, cost minim de implementare.
4. **Șters** `14.html` și `15.html` de la rădăcină (conținut duplicat orfan).
5. Regenerat `blog/*.html` și `nc/*.html` cu generatoarele existente pentru consistență — fără alte schimbări de conținut.

## Fișiere modificate
- `index.html`, `despre.html`, `barbati.html`, `femei.html`, `terapie-cuplu.html`, `adictii.html`, `contact.html`, `pentru-terapeuti.html`, `blog.html` — schema `ProfessionalService`+`Person` adăugată
- `gen-articole.py` — funcții `extrage_faq()` + `faq_schema_html()`, template extins
- `blog/diferenta-de-libido-in-cuplu.html` — regenerat, include acum `FAQPage` (5 întrebări)
- `blog/*.html` (celelalte 6) — regenerate, fără FAQ (nu au secțiune sursă)
- `nc/*.html` — regenerate, fără modificări de conținut
- `sitemap.xml` — `lastmod` actualizat pentru `/blog` și `/note-din-cabinet`
- `llms.txt` — fișier nou
- `14.html`, `15.html` — șterse

## De decis / de la Edi
- **URL-urile exacte de profil** (Hilio, pleso.me, la-psiholog.ro, ROmedic) — le adaug ca `sameAs` în schema `Person` pe toate paginile într-o trecere ulterioară, o dată ce le trimiți.
- **Restructurarea celor 6 articole vechi** (fără H2, fără FAQ) — necesită rescriere de conținut conform skill 04, nu doar schema. De discutat prioritate.

## Deploy
1. Copiază conținutul arhivei peste repo (arhiva include ștergerea `14.html`/`15.html` — la copiere manuală, șterge-le explicit dacă nu se suprascriu automat).
2. `git add -A && git commit && git push` (Netlify deploy automat).
