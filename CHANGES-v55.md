# v55 — 2026-11-04 — fix-uri SEO

- index: title „Psihoterapeut București, Sector 1 · Edi Vlaston”; meta/og/twitter description fără poziționarea v5 („bărbați cu probleme relaționale”)
- blog: title + meta description noi (fără „psihologie masculină”); categoria „Psihologie masculină” → „Emoții” (articole.json, blog.html, cum-sa-recunosti-ce-simti)
- schema: `sameAs` (Facebook, Instagram, Hilio, Google Maps) pe Person în toate paginile principale + generatorul de articole; `hasMap` pe ProfessionalService
- gen-articole.py: autorul articolelor primește `sameAs` (se aplică la următoarea regenerare)
