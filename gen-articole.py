#!/usr/bin/env python3
"""
Generator pagini statice pentru articolele de blog.
Citeste articole.json si produce cate o pagina /blog/{id}.html cu:
  - tot textul articolului in HTML static (vizibil pentru Google si crawlerele AI)
  - meta tags corecte (title, description, OG)
  - schema Article + Person JSON-LD direct in HTML
  - CTA spre Calendly
  - linking intern spre alte articole + pagini serviciu

FLUX:
  1. adaugi/editezi articolul in articole.json
  2. rulezi: python3 gen-articole.py
  3. git add -A && commit && push
"""
import json, re, os, html, datetime

BASE = "https://edivlaston.ro"
IMG = f"{BASE}/edi-vlaston.webp"
OUTDIR = "blog"
TODAY = datetime.date.today().isoformat()

def text_din_continut(continut, n=155):
    t = re.sub(r"<[^>]+>", " ", continut)
    t = re.sub(r"\s+", " ", t).strip()
    return (t[:n].rsplit(" ", 1)[0] + "…") if len(t) > n else t

def extrage_faq(continut):
    """Cauta sectiunea <h2>Intrebari frecvente</h2> si extrage perechile
    <h3>intrebare</h3><p>raspuns</p> care urmeaza, pana la urmatorul H2 sau finalul textului.
    Returneaza o lista de tupluri (intrebare, raspuns) curatate de tag-uri HTML."""
    m = re.search(r"<h2>\s*[IÎ]ntreb[aă]ri frecvente\s*</h2>(.*?)(?=<h2>|$)", continut, re.S | re.I)
    if not m:
        return []
    sectiune = m.group(1)
    perechi = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", sectiune, re.S)
    faq = []
    for q, a in perechi:
        q_curat = re.sub(r"<[^>]+>", "", q).strip()
        a_curat = re.sub(r"<[^>]+>", " ", a)
        a_curat = re.sub(r"\s+", " ", a_curat).strip()
        if q_curat and a_curat:
            faq.append((q_curat, a_curat))
    return faq

def faq_schema_html(faq):
    """Construieste blocul <script type=application/ld+json> pentru FAQPage.
    Returneaza string gol daca nu exista FAQ."""
    if not faq:
        return ""
    entitati = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faq
    ]
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entitati,
    }
    return (
        '  <!-- Schema FAQPage (auto-extras din sectiunea Intrebari frecvente) -->\n'
        '  <script type="application/ld+json">\n'
        + json.dumps(schema, ensure_ascii=False, indent=2)
        + '\n  </script>\n'
    )

arts = json.load(open("articole.json"))

os.makedirs(OUTDIR, exist_ok=True)
# curat paginile vechi
for f in os.listdir(OUTDIR):
    if f.endswith(".html"):
        os.remove(os.path.join(OUTDIR, f))

NAV = '''<nav id="nav">
  <a href="/" class="nav-brand">Edi Vlaston<span>.</span></a>
  <div class="nav-links">
    <a href="/barbati">Pentru Ei</a>
    <a href="/femei">Pentru Ele</a>
    <a href="/terapie-cuplu">Terapie de cuplu</a>
    <a href="/despre">Despre</a>
    <a href="/blog" class="active">Blog</a>
    <a href="/note-din-cabinet">Note din Cabinet</a>
    <a href="/intrebari-frecvente">Întrebări Frecvente</a>
    <a href="/preturi">Prețuri</a>
    <a href="/contact">Contact</a>
    <a href="https://calendly.com/eduard-vlaston-eiv3" onclick="Calendly.initPopupWidget({url:'https://calendly.com/eduard-vlaston-eiv3'}); return false;" class="nav-cta">Rezervă o primă ședință</a>
  </div>
  <button class="hamburger" id="hamburger" onclick="toggleMenu()" aria-label="Meniu">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="mobile-menu" id="mobile-menu">
  <a href="/barbati" onclick="closeMenu()">Pentru Ei</a>
  <a href="/femei" onclick="closeMenu()">Pentru Ele</a>
  <a href="/terapie-cuplu" onclick="closeMenu()">Terapie de cuplu</a>
  <a href="/despre" onclick="closeMenu()">Despre</a>
  <a href="/blog" onclick="closeMenu()">Blog</a>
  <a href="/note-din-cabinet" onclick="closeMenu()">Note din Cabinet</a>
  <a href="/intrebari-frecvente" onclick="closeMenu()">Întrebări Frecvente</a>
  <a href="/preturi" onclick="closeMenu()">Prețuri</a>
  <a href="/contact" onclick="closeMenu()">Contact</a>
  <a href="tel:+40744370179" class="mobile-phone" onclick="closeMenu()">📞 0744 370 179</a>
  <a href="https://calendly.com/eduard-vlaston-eiv3" onclick="Calendly.initPopupWidget({url:'https://calendly.com/eduard-vlaston-eiv3'}); closeMenu(); return false;" class="mobile-cta">Rezervă o primă ședință</a>
</div>'''

FOOTER = '''<!-- Bara de contact -->
<div style="text-align:center;padding:30px 20px;border-top:1px solid var(--stone);background:var(--sand)">
  <p style="font-size:.7rem;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:14px">Sună sau scrie direct</p>
  <div style="display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:10px 16px;font-size:.92rem">
    <a href="tel:+40744370179" style="color:var(--terra);font-weight:500;text-decoration:none">0744 370 179</a>
    <span style="color:var(--stone)" aria-hidden="true">·</span>
    <a href="https://wa.me/40744370179" target="_blank" rel="noopener" style="color:var(--terra);font-weight:500;text-decoration:none">WhatsApp</a>
    <span style="color:var(--stone)" aria-hidden="true">·</span>
    <a href="https://t.me/edivlaston" target="_blank" rel="noopener" style="color:var(--terra);font-weight:500;text-decoration:none">Telegram</a>
    <span style="color:var(--stone)" aria-hidden="true">·</span>
    <a href="mailto:office@edivlaston.ro" style="color:var(--terra);font-weight:500;text-decoration:none">office@edivlaston.ro</a>
  </div>
</div>
<footer>
  <div class="container">
    <div class="footer-in">
      <div class="footer-brand">Edi Vlaston<span>.</span></div>
        <a href="mailto:office@edivlaston.ro">office@edivlaston.ro</a></div>
      <a href="/confidentialitate" style="display:block;text-align:center;font-size:.78rem;color:var(--muted);margin:8px 0;">Politica de confidențialitate</a>
      <span class="footer-copy">© 2026 Cabinet Individual de Psihologie · Cod 22334</span>
    </div>
  </div>
</footer>
<!-- Calendly Event Tracking -->
<script>
window.addEventListener('message', function(e) {
  if (e.data.event && e.data.event.indexOf('calendly') === 0) {
    if (e.data.event === 'calendly.event_scheduled') {
      if (typeof gtag === 'function') {
        gtag('event', 'programare_calendly', {
          'event_category': 'conversie',
          'event_label': 'Calendly Programare Finalizata'
        });
        gtag('event', 'conversion', {
          'send_to': 'AW-17654719970/VtMcCPnxyc8cEOLLtuJB'
        });
      }
      if (typeof fbq === 'function') {
        fbq('track', 'Schedule', {content_name: 'Programare_Finalizata'});
      }
    }
  }
});
</script>
<!-- End Calendly Event Tracking -->
<script>
/* Click WhatsApp / telefon / telegram / email -> GA4 + Meta */
document.addEventListener('click', function (e) {
  var a = e.target;
  while (a && a.tagName !== 'A') a = a.parentElement;
  if (!a || !a.href) return;
  var h = a.href, canal = null;
  if (h.indexOf('wa.me') !== -1 || h.indexOf('api.whatsapp.com') !== -1) canal = 'whatsapp';
  else if (h.indexOf('tel:') === 0) canal = 'telefon';
  else if (h.indexOf('t.me/') !== -1) canal = 'telegram';
  else if (h.indexOf('mailto:') === 0) canal = 'email';
  if (!canal) return;
  if (typeof gtag === 'function') {
    gtag('event', 'contact_' + canal, {'event_category': 'contact', 'event_label': canal});
  }
  if (typeof fbq === 'function') fbq('track', 'Contact', {content_name: canal});
}, true);
</script>'''

PAGE = '''<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="{base}/blog/{id}">
  <meta name="description" content="{desc}">
  <title>{title}</title>
  <meta property="og:type" content="article">
  <meta property="og:title" content="{ogtitle}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{base}/blog/{id}">
  <meta property="og:image" content="{img}">
  <meta name="twitter:card" content="summary_large_image">
  <!-- Google Tag (Analytics + Ads) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-17654719970"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-2W226C545N');
    gtag('config', 'AW-17654719970');
  </script>
  <meta name="google-site-verification" content="z14BQ7ieyIuxJ1hAWddXO5ljOwfq92d7fcFSMoB_gn0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/style.css">
  <!-- Schema Article + Person -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": {schema_titlu},
    "description": {schema_desc},
    "datePublished": "{data}",
    "dateModified": "{data}",
    "image": "{img}",
    "author": {{
      "@type": "Person",
      "name": "Edi Vlaston",
      "jobTitle": "Psihoterapeut",
      "url": "{base}/despre"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Edi Vlaston · Cabinet Individual de Psihologie",
      "logo": {{"@type": "ImageObject", "url": "{img}"}}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "{base}/blog/{id}"
    }}
  }}
  </script>
{faq_schema}  <style>
    .art-wrap{{max-width:720px;margin:0 auto;padding:0 24px}}
    .art-header{{padding:120px 0 0;text-align:center}}
    .art-cat{{font-size:.7rem;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--terra);margin-bottom:16px}}
    .art-header h1{{font-family:var(--serif);font-size:clamp(1.8rem,4vw,2.8rem);font-weight:400;line-height:1.2;color:var(--ink);margin-bottom:18px}}
    .art-date{{font-size:.82rem;color:var(--light)}}
    .art-body{{padding:48px 0;font-size:1.08rem;color:var(--warm);line-height:1.9;font-weight:300}}
    .art-body p{{margin-bottom:20px}}
    .art-body h2{{font-family:var(--serif);font-size:1.5rem;font-weight:500;color:var(--ink);margin:36px 0 14px}}
    .art-body h3{{font-family:var(--serif);font-size:1.25rem;font-weight:500;color:var(--ink);margin:28px 0 12px}}
    .art-body strong{{color:var(--ink);font-weight:500}}
    .art-body ul,.art-body ol{{margin:0 0 20px 24px}}
    .art-body li{{margin-bottom:8px}}
    .art-cta{{margin:48px 0;padding:36px;background:var(--sand);border-radius:8px;text-align:center}}
    .art-cta h3{{font-family:var(--serif);font-size:1.4rem;font-weight:400;color:var(--ink);margin-bottom:12px}}
    .art-cta p{{font-size:.95rem;color:var(--warm);line-height:1.7;margin-bottom:24px;max-width:480px;margin-left:auto;margin-right:auto}}
    .art-related{{padding:48px 0;border-top:1px solid var(--stone)}}
    .art-related-label{{font-size:.72rem;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--terra);margin-bottom:24px;text-align:center}}
    .art-related-grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
    .art-related-card{{background:var(--white);border:1px solid var(--stone);border-radius:8px;padding:24px;text-decoration:none;transition:border-color .2s,transform .2s}}
    .art-related-card:hover{{border-color:var(--bark);transform:translateY(-3px)}}
    .art-related-card .cat{{font-size:.62rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--terra);margin-bottom:8px;display:block}}
    .art-related-card h4{{font-family:var(--serif);font-size:1.05rem;font-weight:500;color:var(--ink);line-height:1.35}}
    .art-back{{display:inline-block;margin:24px 0;font-size:.82rem;color:var(--terra);text-decoration:none;letter-spacing:.04em}}
    @media(max-width:680px){{.art-related-grid{{grid-template-columns:1fr}}.art-header{{padding:90px 0 0}}}}
  </style>
<script>
function toggleMenu(){{var m=document.getElementById('mobile-menu'),b=document.getElementById('hamburger');if(!m||!b)return;b.classList.toggle('open');m.classList.toggle('open');document.body.style.overflow=m.classList.contains('open')?'hidden':'';}}
function closeMenu(){{var m=document.getElementById('mobile-menu'),b=document.getElementById('hamburger');if(m)m.classList.remove('open');if(b)b.classList.remove('open');document.body.style.overflow='';}}
</script>
</head>
<body>
{nav}

<article class="art-wrap">
  <div class="art-header">
    <div class="art-cat">{categorie}</div>
    <h1>{titlu}</h1>
    <div class="art-date">{data_ro}</div>
  </div>

  <div class="art-body">
{continut}
  </div>

  <div class="art-cta">
    <h3>Dacă te-ai recunoscut în ce ai citit</h3>
    <p>Prima ședință e un prilej de a vedea dacă are sens să continuăm. Fără presiune să decizi azi.</p>
    <a href="https://calendly.com/eduard-vlaston-eiv3" onclick="Calendly.initPopupWidget({{url:'https://calendly.com/eduard-vlaston-eiv3'}}); return false;" class="btn btn-primary">Rezervă o primă ședință</a>
  </div>

  <div class="art-related">
    <div class="art-related-label">Citește mai departe</div>
    <div class="art-related-grid">
{related}
    </div>
  </div>

  <a href="/blog" class="art-back">← Toate articolele</a>
</article>

<!-- Calendly -->
<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>

{footer}
</body>
</html>
'''

LUNI = {1:"ianuarie",2:"februarie",3:"martie",4:"aprilie",5:"mai",6:"iunie",
        7:"iulie",8:"august",9:"septembrie",10:"octombrie",11:"noiembrie",12:"decembrie"}

def data_romaneasca(iso):
    try:
        d = datetime.date.fromisoformat(iso)
        return f"{d.day} {LUNI[d.month]} {d.year}"
    except:
        return iso

for i, a in enumerate(arts):
    aid = a["id"]
    titlu = a["titlu"]
    categorie = a.get("categorie", "")
    data = a.get("data", TODAY)
    desc = a.get("rezumat") or text_din_continut(a["continut"])
    continut = a["continut"]

    # Articolele related = celelalte 2-3 articole
    related_arts = [x for x in arts if x["id"] != aid][:2]
    related_html = ""
    for r in related_arts:
        related_html += f'''      <a href="/blog/{r['id']}" class="art-related-card">
        <span class="cat">{html.escape(r.get('categorie',''))}</span>
        <h4>{html.escape(r['titlu'])}</h4>
      </a>
'''

    full_title = f"{titlu} · Edi Vlaston Psihoterapeut București"
    if len(full_title) > 60:
        full_title = f"{titlu[:45]}… · Edi Vlaston"

    faq = extrage_faq(continut)

    page = PAGE.format(
        base=BASE, id=aid, img=IMG,
        title=html.escape(full_title),
        ogtitle=html.escape(titlu),
        desc=html.escape(desc),
        schema_titlu=json.dumps(titlu, ensure_ascii=False),
        schema_desc=json.dumps(desc, ensure_ascii=False),
        data=data,
        data_ro=data_romaneasca(data),
        categorie=html.escape(categorie),
        titlu=html.escape(titlu),
        continut=continut,
        related=related_html,
        faq_schema=faq_schema_html(faq),
        nav=NAV, footer=FOOTER,
    )
    open(os.path.join(OUTDIR, f"{aid}.html"), "w", encoding="utf-8").write(page)

print(f"OK — {len(arts)} pagini statice in /{OUTDIR}/")
for a in arts:
    faq = extrage_faq(a["continut"])
    print(f"  {BASE}/blog/{a['id']}  (FAQ: {len(faq)} intrebari)")
