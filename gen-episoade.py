#!/usr/bin/env python3
"""
Generator pagini statice pentru Note din Cabinet.
Citeste note-din-cabinet.json si produce:
  1. cate o pagina statica COMPLETA /nc/{episod}.html cu tot textul episodului in HTML
     (vizibil pentru Google si crawlerele AI, OG tags corecte pentru social)
  2. sitemap.xml actualizat (pagini + articole + episoade)

FLUX LA UN EPISOD NOU:
  1. adaugi episodul in note-din-cabinet.json (cu publicat:true)
  2. rulezi: python3 gen-episoade.py
  3. git add -A && commit && push

LINK DE FOLOSIT IN RECLAME: https://edivlaston.ro/note-din-cabinet/6
(serveste direct pagina statica a episodului, cu tot textul)
"""
import json, re, os, datetime, html

BASE = "https://edivlaston.ro"
IMG  = f"{BASE}/edi-vlaston.webp"
TODAY = datetime.date.today().isoformat()
OUTDIR = "nc"

LUNI = {1:"ianuarie",2:"februarie",3:"martie",4:"aprilie",5:"mai",6:"iunie",
        7:"iulie",8:"august",9:"septembrie",10:"octombrie",11:"noiembrie",12:"decembrie"}
def data_ro(iso):
    try:
        d = datetime.date.fromisoformat(iso)
        return f"{d.day} {LUNI[d.month]} {d.year}"
    except: return iso

def text_din_continut(continut, n=155):
    t = re.sub(r"<[^>]+>", " ", continut)
    t = re.sub(r"\s+", " ", t).strip()
    return (t[:n].rsplit(" ", 1)[0] + "…") if len(t) > n else t

eps = json.load(open("note-din-cabinet.json"))
eps = [e for e in eps if e.get("publicat") is not False]
eps.sort(key=lambda e: e["episod"])

os.makedirs(OUTDIR, exist_ok=True)
for f in os.listdir(OUTDIR):
    if f.endswith(".html"):
        os.remove(os.path.join(OUTDIR, f))

NAV = '''<nav id="nav">
  <a href="/" class="nav-brand">Edi Vlaston<span>.</span></a>
  <div class="nav-links">
    <a href="/barbati">Pentru Ei</a>
    <a href="/femei">Pentru Ele</a>
    <a href="/despre">Despre</a>
    <a href="/blog">Blog</a>
    <a href="/note-din-cabinet" class="active">Note din Cabinet</a>
    <a href="/intrebari-frecvente">Întrebări Frecvente</a>
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
  <a href="/despre" onclick="closeMenu()">Despre</a>
  <a href="/blog" onclick="closeMenu()">Blog</a>
  <a href="/note-din-cabinet" onclick="closeMenu()">Note din Cabinet</a>
  <a href="/intrebari-frecvente" onclick="closeMenu()">Întrebări Frecvente</a>
  <a href="/contact" onclick="closeMenu()">Contact</a>
  <a href="tel:+40744370179" class="mobile-phone" onclick="closeMenu()">📞 0744 370 179</a>
  <a href="https://calendly.com/eduard-vlaston-eiv3" onclick="Calendly.initPopupWidget({url:'https://calendly.com/eduard-vlaston-eiv3'}); closeMenu(); return false;" class="mobile-cta">Rezervă o primă ședință</a>
</div>'''

FOOTER = '''<footer>
  <div class="container">
    <div class="footer-in">
      <div class="footer-brand">Edi Vlaston<span>.</span></div>
        <a href="mailto:edivlaston@gmail.com">edivlaston@gmail.com</a></div>
      <a href="/confidentialitate" style="display:block;text-align:center;font-size:.78rem;color:var(--muted);margin:8px 0;">Politica de confidențialitate</a>
      <span class="footer-copy">© 2026 Cabinet Individual de Psihologie · Cod 22334</span>
    </div>
  </div>
</footer>'''

PAGE = '''<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="{base}/note-din-cabinet/{ep}">
  <meta name="description" content="{desc}">
  <title>{title}</title>
  <meta property="og:type" content="article">
  <meta property="og:title" content="{ogtitle}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{base}/note-din-cabinet/{ep}">
  <meta property="og:image" content="{img}">
  <meta name="twitter:card" content="summary_large_image">
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
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": {schema_titlu},
    "description": {schema_desc},
    "datePublished": "{data}",
    "image": "{img}",
    "author": {{"@type": "Person", "name": "Edi Vlaston", "jobTitle": "Psihoterapeut", "url": "{base}/despre"}},
    "publisher": {{"@type": "Person", "name": "Edi Vlaston"}},
    "mainEntityOfPage": {{"@type": "WebPage", "@id": "{base}/note-din-cabinet/{ep}"}},
    "isPartOf": {{"@type": "CreativeWorkSeries", "name": "Note din Cabinet"}}
  }}
  </script>
  <style>
    .nc-wrap{{max-width:720px;margin:0 auto;padding:0 24px}}
    .nc-header{{padding:120px 0 0;text-align:center}}
    .nc-cat{{font-size:.7rem;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--terra);margin-bottom:16px}}
    .nc-header h1{{font-family:var(--serif);font-size:clamp(1.7rem,3.6vw,2.6rem);font-weight:400;line-height:1.22;color:var(--ink);margin-bottom:12px}}
    .nc-episub{{font-size:.95rem;color:var(--muted);margin-bottom:14px;letter-spacing:.02em}}
    .nc-date{{font-size:.82rem;color:var(--light)}}
    .nc-body{{padding:44px 0;font-family:var(--serif);font-size:1.18rem;color:var(--ink);line-height:1.85;font-weight:400}}
    .nc-body p{{margin-bottom:16px}}
    .nc-body .ep-inner{{color:var(--warm);font-style:italic;padding-left:18px;border-left:2px solid var(--sand);margin:16px 0}}
    .nc-body em{{font-style:italic;color:var(--warm)}}
    .nc-body .ep-sep{{border:none;border-top:1px solid var(--stone);width:60px;margin:26px auto;opacity:.7}}
    .nc-body .ep-disclaimer{{font-size:.92rem;color:var(--muted);font-style:italic;line-height:1.7;margin-top:8px}}
    .nc-sub{{margin:40px 0;padding:28px;background:var(--sand);border-radius:8px}}
    .nc-sub .lbl{{font-size:.72rem;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--terra);margin-bottom:8px}}
    .nc-sub p{{font-size:.92rem;color:var(--warm);line-height:1.7;margin-bottom:18px}}
    .nc-nav{{display:flex;justify-content:space-between;gap:12px;padding:28px 0;border-top:1px solid var(--stone)}}
    .nc-nav a{{font-size:.82rem;color:var(--terra);text-decoration:none;letter-spacing:.03em;padding:9px 18px;border:1px solid var(--stone);border-radius:30px;transition:border-color .2s}}
    .nc-nav a:hover{{border-color:var(--bark)}}
    .nc-nav a.disabled{{opacity:.3;pointer-events:none}}
    .nc-back{{display:inline-block;margin:20px 0;font-size:.82rem;color:var(--terra);text-decoration:none}}
    @media(max-width:680px){{.nc-header{{padding:90px 0 0}}.nc-wrap{{padding:0 20px}}}}
  </style>
<script>
function toggleMenu(){{var m=document.getElementById('mobile-menu'),b=document.getElementById('hamburger');if(!m||!b)return;b.classList.toggle('open');m.classList.toggle('open');document.body.style.overflow=m.classList.contains('open')?'hidden':'';}}
function closeMenu(){{var m=document.getElementById('mobile-menu'),b=document.getElementById('hamburger');if(m)m.classList.remove('open');if(b)b.classList.remove('open');document.body.style.overflow='';}}
</script>
</head>
<body>
{nav}

<article class="nc-wrap">
  <div class="nc-header">
    <div class="nc-cat">Note din Cabinet · {personaj}</div>
    <h1>{titlu}</h1>
    <div class="nc-episub">{subtitlu}</div>
    <div class="nc-date">{data_ro}</div>
  </div>

  <div class="nc-body">
{continut}
  </div>

  <div class="nc-sub">
    <div class="lbl">Episoade în avans</div>
    <p>Primește fiecare episod nou cu 2-3 zile înainte de publicare.</p>
    <div id="form-modal-wrap">
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <input type="text" id="modal-nume" placeholder="Prenumele tău" style="flex:1;min-width:140px;padding:11px 14px;border:1px solid var(--stone);background:var(--white);color:var(--ink);font-family:var(--sans);font-size:.9rem;border-radius:4px;outline:none">
        <input type="email" id="modal-email" placeholder="Adresa de email" style="flex:2;min-width:180px;padding:11px 14px;border:1px solid var(--stone);background:var(--white);color:var(--ink);font-family:var(--sans);font-size:.9rem;border-radius:4px;outline:none">
        <button onclick="trimiteAbonare()" style="padding:11px 20px;background:var(--terra);color:var(--white);border:none;font-family:var(--sans);font-size:.9rem;font-weight:500;border-radius:4px;cursor:pointer;white-space:nowrap">Abonează-mă</button>
      </div>
      <p style="font-size:.75rem;color:var(--muted);margin-top:10px">Fără spam. Te dezabonezi oricând.</p>
    </div>
    <div id="form-modal-confirmare" style="display:none">
      <p style="font-size:.92rem;color:var(--ink);line-height:1.7">Bine ai venit în listă. Următorul episod ajunge direct la tine.</p>
    </div>
  </div>

  <div class="nc-nav">
    {prev_link}
    {next_link}
  </div>

  <a href="/note-din-cabinet" class="nc-back">← Toate episoadele</a>
</article>

<link href="https://assets.calendly.com/assets/external/widget.css" rel="stylesheet">
<script src="https://assets.calendly.com/assets/external/widget.js" async></script>

{footer}
<script>
function trimiteAbonare() {{
  var nume = document.getElementById('modal-nume').value.trim();
  var email = document.getElementById('modal-email').value.trim();
  if (!email) {{ alert('Te rog completează adresa de email.'); return; }}
  var btn = document.querySelector('#form-modal-wrap button');
  btn.textContent = 'Se trimite...'; btn.disabled = true;
  fetch('https://script.google.com/macros/s/AKfycbx25PVLvMgUgVACP2ReYX4XX8TP5gq_YbLWCQTvjt98bpR41Q5oORgoEChGgjkePNnKIA/exec', {{
    method: 'POST', headers: {{'Content-Type': 'application/json'}},
    body: JSON.stringify({{nume: nume, email: email, pagina: '/note-din-cabinet/{ep}'}})
  }})
  .then(function(r){{ return r.json(); }})
  .then(function(){{
    document.getElementById('form-modal-wrap').style.display = 'none';
    document.getElementById('form-modal-confirmare').style.display = 'block';
    if (typeof gtag === 'function') gtag('event', 'abonare_lista', {{'event_category': 'lead'}});
    if (typeof fbq === 'function') fbq('track', 'Lead', {{content_name: 'Abonare_Note_Cabinet'}});
  }})
  .catch(function(){{ btn.textContent = 'Abonează-mă'; btn.disabled = false; alert('A apărut o eroare. Te rog încearcă din nou.'); }});
}}
</script>
</body>
</html>
'''

for i, e in enumerate(eps):
    ep = e["episod"]
    titlu = e["titlu"]
    personaj = e.get("personaj", "")
    subtitlu = e.get("subtitlu", "")
    data = e.get("data", TODAY)
    desc = e.get("hook") or subtitlu or text_din_continut(e["continut"])
    continut = e["continut"]

    full_title = f"{titlu} · Note din Cabinet"
    if len(full_title) > 60:
        full_title = f"{titlu[:42]}… · Note din Cabinet"

    prev_ep = eps[i-1] if i > 0 else None
    next_ep = eps[i+1] if i < len(eps)-1 else None
    prev_link = (f'<a href="/note-din-cabinet/{prev_ep["episod"]}">← Episodul anterior</a>'
                 if prev_ep else '<a class="disabled">← Episodul anterior</a>')
    next_link = (f'<a href="/note-din-cabinet/{next_ep["episod"]}">Episodul următor →</a>'
                 if next_ep else '<a class="disabled">Episodul următor →</a>')

    page = PAGE.format(
        base=BASE, ep=ep, img=IMG,
        title=html.escape(full_title),
        ogtitle=html.escape(f"{titlu} — {personaj}".strip(" —")),
        desc=html.escape(desc),
        schema_titlu=json.dumps(titlu, ensure_ascii=False),
        schema_desc=json.dumps(desc, ensure_ascii=False),
        data=data, data_ro=data_ro(data),
        personaj=html.escape(personaj),
        titlu=html.escape(titlu),
        subtitlu=html.escape(subtitlu),
        continut=continut,
        prev_link=prev_link, next_link=next_link,
        nav=NAV, footer=FOOTER,
    )
    open(os.path.join(OUTDIR, f"{ep}.html"), "w", encoding="utf-8").write(page)

# ---- sitemap complet (pagini + articole + episoade) ----
arts = json.load(open("articole.json"))
pagini = [
    ("/", "monthly", "1.0", "2026-06-27"),
    ("/barbati", "monthly", "0.9", "2026-06-27"),
    ("/femei", "monthly", "0.8", "2026-06-27"),
    ("/adictii", "monthly", "0.8", "2026-04-28"),
    ("/despre", "monthly", "0.7", "2026-06-27"),
    ("/blog", "weekly", "0.8", TODAY),
    ("/note-din-cabinet", "weekly", "0.8", TODAY),
    ("/intrebari-frecvente", "monthly", "0.7", "2026-06-27"),
    ("/contact", "monthly", "0.6", "2026-04-28"),
    ("/pentru-terapeuti", "monthly", "0.6", "2026-04-28"),
]
lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
def url(loc, lm, cf, pr):
    return ["  <url>", f"    <loc>{loc}</loc>", f"    <lastmod>{lm}</lastmod>",
            f"    <changefreq>{cf}</changefreq>", f"    <priority>{pr}</priority>", "  </url>"]
for cale, cf, pr, lm in pagini:
    lines += url(BASE + cale, lm, cf, pr)
for a in arts:
    lines += url(f"{BASE}/blog/{a['id']}", a.get("data", TODAY), "monthly", "0.7")
for e in eps:
    lines += url(f"{BASE}/note-din-cabinet/{e['episod']}", e.get("data", TODAY), "monthly", "0.7")
lines.append("</urlset>")
open("sitemap.xml", "w", encoding="utf-8").write("\n".join(lines) + "\n")

print(f"OK — {len(eps)} pagini episoade in /{OUTDIR}/")
print(f"Sitemap: {len(pagini)} pagini + {len(arts)} articole + {len(eps)} episoade = {len(pagini)+len(arts)+len(eps)} URL-uri")
