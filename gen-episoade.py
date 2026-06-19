#!/usr/bin/env python3
"""
Generator pentru Note din Cabinet.
Citeste note-din-cabinet.json si produce:
  1. cate un fisier static /nc/{episod}.html cu OG tags corecte (titlu, descriere, imagine)
     -> preview corect pe Facebook/WhatsApp/Instagram cand dai link la episod
  2. sitemap.xml actualizat cu toate episoadele publicate

FLUX LA UN EPISOD NOU:
  1. adaugi episodul in note-din-cabinet.json (cu publicat:true)
  2. optional: pui un camp "hook" (1 fraza) — devine descrierea din preview-ul de social
  3. rulezi:  python3 gen-episoade.py
  4. git add -A && commit && push
Atat. Nimic manual in HTML.

LINK DE FOLOSIT IN RECLAME:  https://edivlaston.ro/nc/6
(redirecteaza instant catre /note-din-cabinet/6 care deschide episodul)
"""
import json, re, os, datetime, html

BASE = "https://edivlaston.ro"
IMG  = f"{BASE}/edi-vlaston.webp"
TODAY = datetime.date.today().isoformat()
OUTDIR = "nc"

def text_din_continut(continut, n=155):
    t = re.sub(r"<[^>]+>", " ", continut)
    t = re.sub(r"\s+", " ", t).strip()
    return (t[:n].rsplit(" ", 1)[0] + "…") if len(t) > n else t

eps = json.load(open("note-din-cabinet.json"))
eps = [e for e in eps if e.get("publicat") is not False]
eps.sort(key=lambda e: e["episod"])

os.makedirs(OUTDIR, exist_ok=True)
# curat stub-uri vechi ca sa nu ramana episoade depublicate
for f in os.listdir(OUTDIR):
    if f.endswith(".html"):
        os.remove(os.path.join(OUTDIR, f))

STUB = """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{base}/note-din-cabinet/{ep}">
<meta property="og:type" content="article">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{base}/note-din-cabinet/{ep}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="refresh" content="0; url={base}/note-din-cabinet/{ep}">
<script>location.replace("{base}/note-din-cabinet/{ep}");</script>
</head>
<body>
<p>Se încarcă episodul… Dacă nu ești redirecționat, <a href="{base}/note-din-cabinet/{ep}">apasă aici</a>.</p>
</body>
</html>
"""

for e in eps:
    ep = e["episod"]
    titlu = e["titlu"]
    desc = e.get("hook") or e.get("subtitlu") or text_din_continut(e["continut"])
    full_title = f"{titlu} · Note din Cabinet · Edi Vlaston"
    og_title = f"{titlu} — {e.get('personaj','')}".strip(" —")
    out = STUB.format(
        title=html.escape(full_title),
        ogtitle=html.escape(og_title),
        desc=html.escape(desc),
        base=BASE, ep=ep, img=IMG,
    )
    open(os.path.join(OUTDIR, f"{ep}.html"), "w", encoding="utf-8").write(out)

# ---- sitemap ----
pagini = [
    ("/", "monthly", "1.0", "2026-06-08"),
    ("/barbati", "monthly", "0.9", "2026-04-28"),
    ("/femei", "monthly", "0.8", "2026-04-28"),
    ("/adictii", "monthly", "0.8", "2026-04-28"),
    ("/despre", "monthly", "0.7", "2026-04-28"),
    ("/blog", "weekly", "0.7", "2026-04-28"),
    ("/note-din-cabinet", "weekly", "0.8", TODAY),
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
for e in eps:
    lines += url(f"{BASE}/note-din-cabinet/{e['episod']}", e.get("data", TODAY), "monthly", "0.7")
lines.append("</urlset>")
open("sitemap.xml", "w", encoding="utf-8").write("\n".join(lines) + "\n")

print(f"OK — {len(eps)} stub-uri in /{OUTDIR}/ + sitemap cu {len(pagini)+len(eps)} URL-uri")
print("Link reclame: " + ", ".join(f"{BASE}/nc/{e['episod']}" for e in eps))
