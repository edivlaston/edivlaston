# CHANGES v24 — 2026-07-20

## Articol nou pe blog: „De ce nu trece anxietatea, deși ai înțeles-o"

Articol de autoritate clinică pe clusterul de achiziție **anxietate** (§8 BrandVoice),
cu punte spre conflictul de adaptare. Miezul: *insight ≠ schimbare* — și, mai ascuțit,
înțelegerea ca formă de evitare la bărbatul analitic (Segment D).

- **id / URL:** `/blog/de-ce-nu-trece-anxietatea`
- **Categorie:** Anxietate (categorie nouă — se afișează automat, fără filtru hardcodat)
- **Keyword principal:** de ce nu trece anxietatea
- **Diferențiator clinic:** Gendlin (felt sense) ancorat în tradiția centrată pe persoană —
  întoarce argumentul „talk therapy nu merge la anxietate" în favoarea PCP.
- **Referințe reale, corect atribuite:** Borkovec (teoria evitării), Gendlin (Focusing).
  Fără cifre din surse neverificabile.
- **Fraze de brand:** hook „ai înțeles și tot nu s-a schimbat nimic" +
  explicație v6 „Înțelegerea îți spune unde ești. Nu te și mută."
- **Adresă:** menționează Primăverii (nu Piața Victoriei).
- ~1.430 cuvinte corp + CTA generat automat. Fără emoji, fără AI-isms, fără promisiuni.

## Fișiere modificate
- `articole.json` — articol nou adăugat primul în listă
- `blog.html` — card fallback (no-JS/crawler) adăugat sus în grid
- `blog/de-ce-nu-trece-anxietatea.html` — pagină generată nouă
- `blog/*.html` — toate regenerate (secțiunea „Citește mai departe" include noul articol)
- `sitemap.xml` — URL nou + `/blog` lastmod → 2026-07-20

## De completat manual (opțional)
- Imagine principală (acum placeholder 📖). Câmp `imagine` în articole.json + fișier în /images/blog/.
- Internal links în corp spre /barbati și un episod Note din Cabinet — momentan doar CTA-ul generat.

## Deploy
1. Copiază conținutul arhivei peste repo.
2. `git add -A && git commit && git push` (Netlify face deploy automat).
   NU rula gen-articole.py din nou dacă nu editezi articole.json — paginile sunt deja generate.
