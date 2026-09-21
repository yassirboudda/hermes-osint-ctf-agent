# Deep Threats — techniques digest (from official write-up)

Source corpus: `wu-deep-threats-writeup.md` (+ PDF `wu-deep-threats-writeup.pdf`).  
Official correction write-up (Marinatech / Lianhua / Institut Lotus narrative).

> Réponses/flags = **méthodo** pour futurs CTF fictionnels du même style.  
> Ne jamais submit sans corrélation ≥2 sources + OK humain.

---

## Playbook condensé (chaînes utiles)

| Challenge (titre) | Pattern méthodo | Outils / pivots |
|-------------------|-----------------|-----------------|
| Président | Org → dirigeant → **LinkedIn past roles** | Google, LinkedIn |
| Soupçon / Nouvel allié | Employee roster → **X timeline dates** ; LinkedIn post → partner site news | Site corp, X, LinkedIn |
| Wesh couz | Photo géoloc : **ouvrir full-res** pour lire pancarte | X media, Maps |
| Portefeuille | Compter items carousel → **view-source** plus fiable que UI | DevTools / curl source |
| L’écolo | Pseudo X → Mastodon → **Wayback profil ancien** | X, Mastodon, Wayback |
| Deal / Coin discret | Wallet Sepolia → Etherscan **tx input/comment** → payeur + ref | Etherscan testnet |
| Doctor Who / Wuan upon a time | Site partenaire → calendrier thèses ; **Reddit** bio parcours | Site univ, Reddit (Rosint) |
| Pas d’ami | Google Docs **share dialog** révèle email auteur (sans envoyer) → wiki + réseau local | Docs, Medium, Qiao |
| Geo / Métal | Wiki nation fictionnelle | Wiki interne |
| Courrier 1/2 | Mail → **Afficher l’original** / headers → IP émetteur | Mail headers |
| French touch / Belle histoire | LNN article + **vidéo** ; wiki Haidong acronyme | LNN, wiki |
| Doctrine / Tableau / Plume | Rapports PDF institut → chapitres / auteurs / gouvernance | Site think-tank |
| Visage familier | Ressemblance LinkedIn → **Wayback** ancien nom d’épouse | LinkedIn, Wayback |
| The creator | WordPress `/?author=N` enum **douce** (IDs bas, pas fuzz massif) | CMS author |
| Jardinier | SOCMINT local (Qiao) → employeur + fraternité via handles | Qiao |
| À table | Photo resto → **carte fan** `lna.maps.space` + landmarks | GEOINT carte custom |
| Anguille / Sésame | IP site → Shodan/Censys → **.onion** ; post-it ASCII → pass ; user = handle Qiao | Shodan passif, dcode |
| Homme occupé / Contrôle | Intranet `.ln` / `.gouv.ln` lois & fiches | Réseau fiction |
| Made in France | Base brevets nationale | Patent DB |
| Non négociable / Précieux | Portail légal + **AI Act / National Intelligence Act** | Legal portal |
| Message intime | Traduction message (ex. chinois) | Traducteur |
| Capital risque / Parts | Corporate registry + SDA contract wording | Registries, PDF |
| Boulette | Adresse HQ FR (La Défense) | Maps / registry |
| Poupées russes | Structure holding / subsidiaries | Corporate graph |
| Courrier 2/2 | Suite headers / pivot mail | Headers |
| Le pacte | Clause contrat « alternative structure / substantially equivalent » | PDF juridique |

---

## Patterns réutilisables (Hermes)

1. **LinkedIn past title** bat souvent le site « about » actuel.  
2. **Full-size image** avant Lens : texte pancarte / EXIF / post-it.  
3. **View-source** pour carrousels / listes dynamiques.  
4. **Wayback** sur profils sociaux (Mastodon) et pages équipe (nom d’épouse).  
5. **On-chain testnet** : memo / input data UTF-8 = flag.  
6. **Google Docs share UI** peut fuiter l’email owner (passif, pas d’envoi).  
7. **Reddit archives** (Rosint) pour parcours universitaire / mentor.  
8. **CMS `?author=`** : soft enum IDs bas — **pas** de fuzz dir.  
9. **Shodan/Censys passif** sur IP site → onion / services.  
10. **OCR sticky note** → ASCII / CyberChef / dcode.  
11. Cartes custom / fan maps d’une nation fictionnelle = GEOINT clé.  
12. Portails `.gouv.*` / brevets / lois = flags « article X ».

## Anti-patterns confirmés (Deep Threats)
- Fuzz / wordlists sur l’infra CTF → ban.  
- Compter à l’œil un carousel animé.  
- S’arrêter au LinkedIn « actuel » sans Wayback / past experience.  
- Ignorer headers mail et memos Etherscan.
