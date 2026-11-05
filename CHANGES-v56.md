# v56 — 2026-11-05 — campanie „Tu cu cine vorbești?” (noiembrie, luna sănătății bărbaților)

- pagină nouă `/cu-cine-vorbesti` (cu-cine-vorbesti.html): formular anonim Netlify `propozitie` (max. 280 caractere, bifă de acord obligatorie, honeypot), casetă de siguranță cu liniile de urgență deasupra butonului, lista „Ce au scris alții”, share WhatsApp + copiază linkul, CTA Calendly cu UTM `utm_source=site&utm_medium=hub&utm_campaign=cu-cine-vorbesti`
- texte: „Fără nume” în loc de „Anonim” în meta/OG/eticheta formularului; scoasă linia 116 123 din caseta de siguranță
- măsurare: doar evenimentul GA4 `propozitie_trimisa`, fără text; fără Meta Pixel pe pagină
- imagine OG: cu-cine-vorbesti-og.png (1200×630, doar întrebarea)
- banner discret „Noiembrie · Tu cu cine vorbești? →” în hero-ul homepage-ului și pe /barbati; dispare automat după 30 noiembrie 2026 (de scos din cod în decembrie)
- sitemap: adăugat /cu-cine-vorbesti; _redirects: /cu-cine-vorbesti.html → /cu-cine-vorbesti

De făcut în Netlify după deploy:
- Forms > formularul `propozitie` > Submission notifications: email către eduard.vlaston@emaconsultings.com (singurul membru al echipei Netlify)
- Moderare: lista de pe pagină se actualizează manual (propozițiile noi se adaugă sus)
