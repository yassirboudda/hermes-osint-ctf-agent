# Source: https://oscarzulu.org/images/2026/04/Write-UP-Medileakv2s.pdf

Write UP Medileakv2s
Voici le Write Up officiel de Medileak v2, CTF OSINT produit par Limoges Métropole et conçu par
Oscar Zulu.
La solution n’étant pas linéaire, la présentation de ce write up a été organisée en catégories qui
suivent le fil de l’enquête.
RAOUL
#Intro
Énoncé :
Un an s'est écoulé depuis l'affaire de la Clinique Yemanji, la fuite de ses fondateurs et la mise aux
enchères des données de santé collectées par l'association Osain.
Pourtant, des questions persistent concernant un personnage qui avait mystérieusement disparu
le 10 juin 2024 à Limoges. En effet, Raoul, notre pharmacien, n'avait laissé aucune trace derrière
lui. Mais son appétit pour les activités lucratives n'est sans doute pas assouvi. Et votre instinct
vous souffle que ce personnage peu scrupuleux n'a peut-être pas fini de faire parler de lui.
Solution :
Pas de difficulté ici, c’est juste pour bien prend en compte le règlement et les outils par les joueurs.

flag : Surtout pas de cloches

#legacy
Énoncé :
Comment retrouver un homme disparu depuis bientot un an, sans avoir laisser de trace ?
Il serait peut être opportun de relire attentivement le Write Up Officiel de Medileak pour se
rappeler de Raoul, de son passé et de ses activités...
Quel était le nom de son laboratoire ?
Format de Flag : Mc Donald's Healthy Food
Solution :
En consultant le Write Up officiel de Medileak (https://oscarzulu.org/wu-medileak/), on peut y voir
que Raoul Reidid avait fondé un laboratoire:
Le flag est: Dr. Revel’s Marvel Oils

#reboot
Énoncé :
Raoul n'a surement pas encore gouté aux joies d'une retraite (bien mal) méritée.
Mais quel est son pseudo sur un réseau social bien connu de partage de vidéo ?
format : unpseudo
Solution :
La recherche d’un reseau social bien connu de partage de video peut être Youtube, Dailymotion
mais aussi Tiktok.
En recherchant Dr Revel sur Tiktotk, on trouve le profil de notre cher docteur qui fait la promo de
ses huiles magiques
Le flag est : drrevelmarveloil

#notcyprus
Énoncé :
Notre pseudo medecin a donc bien rebondit en utilisant les nouveaux codes de communication.
Mais ou se trouvait-il donc le 5 avril 2025 ?
Solution :
Sur son profil tiktok, nous voyons une vidéo intitulée New Life, New Home datée du 05/04.
On y voit un balcon et un immeuble dans le fond.
L’analyse de cet immeuble avec Google Image nous oriente rapidement vers la tour Al Manara
située à Dubai (https://www.skyscrapercenter.com/dubai/al-manara/14186)
On voit donc la tour Al Manara à droite, une autre tour sur la gauche et un bâtiment plus près. En
étudiant une carte, on peut en déduire que nous somme situé à cet endroit:




Le flag est : 25.1846 55.2617

#fanclub
Énoncé :
Raoul a sûrement des admirateurs. Qui est le plus grand fan de Raoul ?
Solution :
Toujours sur le profil TikTok https://www.tiktok.com/@drrevelmarveloil, on peut voir plusieurs
commentaires du compte celestin_aitoubib. Son profil indique qu’il est CEO dans l’entreprise
AITOUBIB, nous allons donc regarder cette entreprise. Une recherche sur Linkedin avec le nom de
l’entreprise nous donne directement le compte de Celestin Marchevend
https://www.linkedin.com/in/celestin-marchevend/

Le flag est : Celestin Marchevend

#backtobusiness
Énoncé :
Quel est le numero de vol que Raoul a pris pour revenir en France ?
Solution :
En utilisant un bon outil de recherche par pseudos (https://usercheck.oscarzulu.org/) nous
trouvons un compte pour drrevel sur le site FlightRadar24. (https://my.flightradar24.com/drrevel)




On y voit deux vols, l’un de Charles de Gaulle vers l’aéroport de Dubai le 15/06/2024 et le vol de
retour le 10/04/2025.
Le flag est: EK73

#PasSympa
Énoncé :
Le départ de Raoul semble un peu précipité…
Trouvez l'initiale et la date du message qui l'a convaincu de partir
Solution :
En nous rendant sur place grâce à l’OIW,




nous trouvons un mystérieux message sur un papier froissé:
Le flag est: Z090425

Employeur providentiel
#NewJob
Énoncé :
Une offre d'emploi providentielle semble attendre Raoul à son retour en France.
Quel est le nom commercial de la société ?

Solution :
Nous avons trouvé précédemment que Celestin Marchevend s’intéressait à Raoul. Une recherche
sur les RS en utilisant le nom de Celestin (ou AITOUBIB) nous remonte un compte bluesky pour
Celestin (https://bsky.app/profile/celestinm.bsky.social)
L’étude de ses réponses nous informe que Raoul ( sous le compte
https://bsky.app/profile/drraoul.bsky.social ) à de nouvelles responsabilités chez AITOUBIB.
Nous voyons plusieurs orthographes pour AITOUBIB, afin de confirmer le nom commercial, nous
allons rechercher le site web de cette société.
Sur son site web https://aitoubib.fr/page/legal/, nous y voyons que le nom est AITOUBIB.
Nous découvrons également l’existence de https://finint.ninja/, ce site nous confime que le nom
commercial est AITOUBIB mais que la dénomination sociale de l’entreprise est MediIIA.
Le flag est: AITOUBIB

#IciCaRecrute
Énoncé :
AITOUBIB recrute !
Quelle est l'url pour "postuler" ?
Solution :
Sur le site web trouvé précédemment, nous voyons dans la page actualités
(https://aitoubib.fr/page/actualites/) un article sur le recrutement d’un CTO
(https://aitoubib.fr/page/offre-demploi-cto/).
Le recrutement semble se faire au travers d’un CTF via la plateforme ctf.iraoul.fr.
Le flag est : https://ctf.iraoul.fr

#TropTard
Énoncé :
Il semble que le poste de CTO soit déjà pourvu...
Dommage...
A quel "groupe" appartient le gagnant ?
Solution :
Nous allons regarder de plus prêt cette plateforme de CTF. Dans la présentation, une des question
peut nous orienter sur une piste:
Q : Ces challenges sont originaux ?
R : Mais Oui ! Vous croyez vraiment que des gens honnêtes comme nous
s'amusent à copier coller des challenges déjà existant ?

Le premier challenge de Stegano (SmallText) nous présente une image. En analysant cette
dernière nous voyons que le propriétaire de l’image n’est pas Raoul mais Mars@Hack 2025.
Cela semble confirmer notre hypothèse que Raoul n’a pas produit les challenges mais simplement
recopié ces derniers. Nous allons donc chercher ce que contient Mars@Hack 2025.
Une recherche Google avec "Mars@Hack" writeup nous remonte un git regroupant tout les
write up des éditions passées de Mars@Hack (https://gitlab.com/marshack)
 Nous y retrouvons l’ensemble des challenges proposés sur la plateforme iraoul et nous permet de
valider rapidement les challenges.
Le flag de fin nous indique que le gagnant est Fastictac de l’équipe Fun Loving Squirrels.
Le flag est : Fun Loving Squirrels

#AvisNégatif
Énoncé :
Mais AITOUBIB ne semble pas complètement "clean"...
Un projet du CEO pourrait lui attirer des problèmes s'il était rendu public.
Combien projète t-il de rémunérer par ordonnance, et quelle augmentation de la marge brute
prévoit-il grâce à la mise en place de son projet ?
Solution :
Nous recherchons sur wayback machine l’existence de précédents archivage de la page aitoubib.fr.
La page a bien été archivée le 09/04/2025
(https://web.archive.org/web/20250409140759/https://aitoubib.fr/). En analysant cette archive
nous y voyons plusieurs informations:
  L’ancienne CTO se nomme Lucie Monlucin
  Le code source de la page nous indique <!-- Cr34t3d by LVC1-F3R -->
Nous allons investiguer sur cette personne.
En pivotant sur son pseudo gràce à https://usercheck.oscarzulu.org/ nous découvrons l’existence
d’un git https://github.com/LVC1-F3R.




On peut y découvrir son CV, ayant changé de poste récemment nous allons regarder si des
modifications récentes ont été apportées à sa page. Il s’avère que 4 commits ont été effectués sur
sa page d’accueil:
Le commit le plus récent nous informe que nous pouvons la contacter sur OIW et qu’elle est assez
remontée contre son ancienne entreprise.




En échangeant avec cette dernière, ellle nous confie avoir stocké des informations avant son
départ sur un drive.



Ce dernier contient 2 documents, le premier est un document interne d’AITOUBIB rédigé par
Celestin Marchevend dans lequel il indique souhaiter employer des médecins étrangers
(notamment en république Tchèque et Hongrie) afin de réduire ses couts.




Le deuxième document est un contrat tyupe écrit en tchèque. Le point 3.2 indique:
3.2. Společnost se zavazuje zaplatit Lékaři odměnu ve výši 200 Kč za
každý podepsaný předpis v souladu s touto smlouvou.

Que l’on peut traduire par La Société s'engage à payer au Médecin des honoraires
de 200 CZK pour chaque ordonnance signée conformément au présent contrat.

Le format attendu étant en €, on converti la somme (arrondi à l'euro le plus proche) à 8€.

Le flag est: 8€ / 43.8%

#NewPartner
Énoncé :
AITOUBIB souhaite ouvrir son capital et s'associer avec une autre entreprise de la région.
Quel est sa dénomination ?
Format : Nom Officiel
Solution :
De retour sur le site aitoubib.fr dans la section des actualités, nous voyons un article sur un
partenariat avec Mediprecog en date du 25/04/2025. Ce dernier nous renvoie vers un site
d’information et un article plus détaillé: https://mednews.tech/2025/04/mediprecog-envisage-un-
investissement-dans-ai-toubib-une-phase-de-test-strategique-en-cours/
L’article indique que Mediprecog est dirigée par la famille Boutevieux. En utilisant le site trouvé
précédemment ( https://finint.ninja), on voit que le Mediprecog est le nom commercial de la
société Boutevieux Medical, dirigée par Jean-Michel Boutevieux.
Le flag est : Boutevieux Medical

#HomeSick
Énoncé :
Où Vesna a t-elle appris des choses difficiles sur son père ?
Solution :
Vesna Dvořáková est la conseillère santé et communication d’AITOUBIB (comme indiqué sur
https://aitoubib.fr/page/equipe/)
Nous pouvons voir qu’elle a commenté un post de Raoul sur Bluesky avec le compte
https://bsky.app/profile/vesnadvorak.bsky.social




Une recherche google avec son pseudo vesnadvorak nous remonte un compte Tripadvisor
(https://www.tripadvisor.com/Profile/VesnaDvorak?fid=d3549aa7-b142-481c-b9ed-
a2093df28f9f):




Sur son avis de la chapelle Saint Aurelien, on peut y lire (traduit du Tchèque):
   Mon père voulait me dire quelque chose de difficile. Il a choisi cette petite
   chapelle pour le faire... Apprendre que notre père se livre à des choses
   innommables juste pour gagner de l'argent est difficile, mais le faire aux yeux
   de Dieu pourrait rendre les choses moins difficiles... Je ne sais pas.




Le flag est : 45.8284, 1.2574
Mediprecog
#Historique
Énoncé :
Quels ont été les premiers produits fabriqués par Boutevieux Medical ?
Solution : Une recherche google sur Jean-Michel Boutevieux nous remonte le site web de sa
société: https://mediprecog.eu/histoire.html
On y voir que les premiers produits fabriqués en 1953 était des sphygmomanomètres mécaniques

Le flag est: sphygmomanomètres mécaniques

#MauvaiseNouvelle
Énoncé :
Des rumeurs sur les dirigeants de l'entreprise semblent avoir fuité dans la presse.
Quelle maladie auraient-ils selon les journalistes ?
Solution : La recherche google : “boutevieux” “maladie” nous remonte un article d’un site de
presse (étrangement ressemblant à mednews.tech) : https://medinews.tech/2025/05/des-
revelations-sur-letat-de-sante-de-la-famille-boutevieux-relancent-le-debat-sur-lavenir-de-
mediprecog/
On y apprend que la famille Boutevieux souffrirait de la maladie de Huntington.
Le flag est: Maladie de Huntington

#Source
Énoncé :
Quel est le pseudonyme de celui qui aurait fait fuiter ces informations ?
Solution : Nécessite #TeamFLS-1 de résolu
Suite à la discussion entre les différents personnages sur le BBS, on a identifié Fastictac comme
étant Lucas Tranolond, qui s’est infiltré au sein de AI TOUBIB en tant que CTO.
Le flag est: Fastictac

#Pression
Énoncé :
Ces rumeurs doivent bien servir un but.
Quelle entreprise a manifesté un intérêt pour racheter Mediprecog ?
Solution : Nous avons vu qu’un faux site de news semble essayer de typosquatter mednews.tech.
Ces derniers ont publié un article à ce sujet : https://mednews.tech/2025/04/mednews-denonce-
une-campagne-de-desinformation-orchestree-par-des-entites-deurope-de-lest/
Ils y dénoncent les intérets de Advanced Medical System et de la sphère d’influence des pays
d’Europe de l’Est.
On y voit également un article ( https://mednews.tech/2025/05/mediprecog-denonce-une-
tentative-de-destabilisation-orchestree-a-travers-des-diagnostics-medicaux-falsifies) sur la fuite
des informations médicales de Mediprecog dans le contexte d’une tentaive de rachat par
Advanced Medical System qui est une filiale française du groupe tchèque Pokročilý Medicínský
Systém.

Le flag est: Advanced Medical System

Advanced Medical System
#MaisonMère
Énoncé :
Advanced Medical System n'est qu'une filiale française d'une société étrangère.
Quel est le site web de la société qui est réellement derrière le rachat ?
Solution : Nous avons vu que Advanced Medical System est une filiale de Pokročilý Medicínský
Systém. Une simple requete sur le nom Pokročilý Medicínský Systém avec l’extension tchèque
nous remonte leur site web: https://pokrocilymedicinskysystem.cz/

Le flag est: pokrocilymedicinskysystem.cz

#MaiSonPère
Énoncé :
Qui dirige la société ?
Solution : Nous savons que Pokročilý Medicínský Systém est la maison mère de Advanced Medical
System. Une recherche sur https://finint.ninja/companies/advanced-medical-system-none/ nous
confirme cette information et nous donne accès aux documents de l’entreprise.
On y note plusieurs informations utiles:
  celle ci est dirigée à 5% par M. Alec BOUCHARDIN et à 5% par M. André FEUILLATON
  celle ci est domiciliée à Chez le Rat 87920 Condat-sur-Vienne France
  les status de l’entreprises sont signés par Zoran Dvořáková réprésentant Pokročilý Medicínský
  Systém en tant que son président.
Le flag est: Zoran Dvořáková

#MaisonChère
Énoncé :
La pierre est toujours un bon investissement.
Quelle maison a t-il acheté ?
Solution : Une recherche sur finint.ninja nous remonte la famille Dvořáková complète liée autour
de la SCI Beau Soleil (https://finint.ninja/companies/sci-beau-soleil-none):
Dans les status de la SCI on peut y voir que Josip et Vesna sont jumeaux. Il est intéressant de
noter que Vesna Dvořáková qui travaille chez AITOUBIB est la fille de Zoran Dvořáková.
Au travers de la SCI Beau Soleil, il a donc acheté Chez le Rat, 87920 Condat-sur-Vienne

Le flag est 45.7877, 1.22758




#RadioGaga
Énoncé :
Comme dans toute opération d'influence, les médias sont un bon moyen de pression.
Vous avez déjà découvert un site web qui semble copier un autre site web.
Mais quelle est le nom de domaine du media "audio" que Zoran semble avoir lancé ?
Solution : En nous déplaçant sur place gràce à l’outil présent dans OIW, nous faisons la rencontre
du jardinier de Zoran. Ce dernier nous apprend que lors d’un apéritif il a évoqué un de ses projets,
une webradio nommée “la voix de l’Europe”.
Nous partons à la recherche de cette webradio, une simple recherche sur lavoixdeleurope.eu nous
permet de trouver cette radio.




Le flag est: lavoixdeleurope.eu

#SoyonsDésinvoltes
Énoncé :
Quel identifiant vous permet de relier 3 sites à Zoran ?
Solution : En analysant le code source de lavoixdeleurope.eu, medinews.tech et
pokrocilymedicinskysystem.cz nous trouvons la trace d’un GTM (Google Tag Manager) servant à
l’analyse de traffic par Google.Le tag est GTM-5J4M3JV8.

Le flag est: GTM-5J4M3JV8

#LesBonsComptes
Énoncé :
Quel comptable aide Zoran dans son projet de rachat ?
Solution : Nous avons vu précédemment que Zoran a signé le document de status d’AMS. Nous
nous intéressons à ce document et en analysant ces metadatas, nous pouvons voir la trace de
l’auteur dans les metadata du document.
Le flag est : Alisha Dy
#Malin
Énoncé :
Suite aux rumeurs de maladie des dirigeants de Mediprecog, AMS réduit son offre de rachat.
Quel % du montant initial propose t-il désormais ?
Solution : Toujours dans le document étudié précédemment nous voyons une signature étrange:




Cette signature est en faite du Base64, après déchiffrement ,on y voit un message partiellement
lisible:
On y découvre une url vers le site alishady.eu:1337 qui semble être la façade illégale du cabinet
comptable.
Une plaquette commerciale est téléchargeable sur le site. Celle-ci ne présente pas beaucoup
d’intéret, en revanche l’URL de téléchargement est intéressante:




En nous rendant à la racine de ce répertoire, nous découvrons une liste de documents clients.
En utilisant le numéro de SIREN d’AMS (098736187) nous avons accès à la nouvelle proposition de
rachat.
Le flag est: 50%

#MeetMe
Énoncé :
Lors de quel evenement le journaliste du podcast a rencontré Zoran ?
Solution : En écoutant la webradio nous entendons un podcast dans lequel échangent deux
personnes que nous avons déja identifié lors du challenge MaiSonPère: Alec BOUCHARDIN et
André FEUILLATON.
Nous retrouvons ces deux personnes sur bluesky avec leurs comptes respectifs
https://bsky.app/profile/did:plc:x3koblszcai6gyj6esd7jmwh et
https://bsky.app/profile/did:plc:okhhtxo4owevwmgwzafioajc
André Feuillaton a participé au salon prago-medica.cz de 2024 où il a rencontré Zoran.
Le flag est: Prago Medica

#Halftime
Énoncé :
Quel est le nom de l'équipe qui a remporté le match où le sportif de haut niveau a rencontré Zoran
?
Solution : Sur son compte bluesky (https://bsky.app/profile/did:plc:x3koblszcai6gyj6esd7jmwh),
nous apprenons que Alec suit la carrière du joueur de hockey Christophe Lalancette et qu’il a
rencontré Zoran lors du troisième match des séries éliminatoires de son équipe.
Sur le site de la NHL (https://www.nhl.com/fr/player/christophe-lalancette-8476959), nous
pouvons voir que Christophe Lalancette évolue actuellement au club HC Plzen:




En recherchant l’historique des matchs de cette équipe, on retrouve rapidement sur le site de
l’équipe le résultat du match dans un article https://www.hcplzen.cz/match/11556. L’équipe de
Lalancette a remporté le match 3 à 0.
Le flag est : HC Skoda Plzen

FLS
#Modem
Énoncé :
Quel est la plateforme utilisée pour joindre les Fun Loving Squirrels ?
Solution : Nous réutilisons notre outil de recherche de profils https://usercheck.oscarzulu.org/ avec
funlovingsquirrels. Celui-ci nous remonte l’existence d’un site web lié au groupe ayant participé au
CTF: https://funlovingsquirrels.wordpress.com/
Sur la page de contact du site, on y voit l’indication :
   You can contact us @ 92.112.194.8:2323


Il faut donc se connecter à cette IP avec un port particulier. Une connexion telnet dans un terminal
suffit à atteindre le BBS (Bulletin board system) utilisé par le groupe




Le flag est : bbs

#Hack
Énoncé :
Quel est le nom de la première société qui a été attaquée avec succès par les Fun Loving Squirrels
?
Solution : En étudiant les échanges des membres de FLS sur le messagerie (touche c) on y voit
l’existence d’une section xsf dans le bbs:
En tapant xfs dans le menu de départ, on obtient accès au menu caché contenant plusieurs lien:




Les liens commencent tous par “bafy”, ce préfixe est caractéristique des CIDs (Content Identifiers)
v1 utilisés dans le système IPFS (InterPlanetary File System), un protocole de stockage de fichiers
en pair-à-pair. Ces liens peuvent être ouvert avec un client lourd ou directement en ligne.
Le premier lien renvoie vers un PDF indiquant l’échec de l’attaque de la cible OKANTIS.
Le second lien indique le succès de l’ataque de Acorn Financial




Le flag est: Acorn Financial

#medileak
Énoncé :
Quel est la date du diagnostic de Jean Michel Boutevieux ?
Solution : Le lien ipfs (bafybeicstsx4twfjzqfb3fzlmnwlllkfbcabxqp2yvt7cjgo5pgipcuygm
) sur le piratage d’AITOUBIB nous renvoie vers un répertoire comprenant plusieurs documents à
étudier:




En recoupant les informations obtenues précédement, nous savons que nous cherchons un
patient diagnostiqué de la maladie de Huntington et étant né le 26/05/1959.
Dans le fichier code_references.csv nous voyons que:
Nous cherchons donc avec le code HD01 et code 05
Dans le fichier patients.csv nous trouvons une correspondance:




Le code patient est donc PT74001.
Dans le fichier diagnostics.csv nous trouvons également Jean-Michel Boutevieux:




La date du diagnostique est donc le 08/03/2022.

Le flag est: 08/03/2022
#TeamFLS-1
Énoncé :
Qui est Fastictac ?
Solution : Sur le BBS des FLS, nous y voyons des échanges autour de l’attaque sur AITOUBIB,
notammment dans le forum général:




Cela nous indique donc que Fastitac travail chez AITOUBIB depuis peu de temps. Nous savons
qu’il a remporté le concours pour être CTO sur la plateforme https://ctf.iraoul.fr/. La page d’équipe
d’AITOUBIB (https://aitoubib.fr/page/equipe/) nous indique que le nouveau CTO est Lucas
Tranolond:
Une recherche avec l’outil https://usercheck.oscarzulu.org/ sur le compte Fastictac nous remonte
sa page github https://github.com/fastictac. En analysant un de ses commits
https://github.com/Fastictac/Fastictac/commit/8693ae8dc5468aca65ce3c68ddcc4f8ec3f3d004.p
atch on y voit également un mail ltrano@ozmail.eu confirmant son identité.

Le flag est: Lucas Tranolond

#TeamFLS-2
Énoncé :
Qui est PsychOspip ?
Solution : Une recherche avec l’outil https://usercheck.oscarzulu.org/ sur le compte PsychOspip
nous remonte sa page steam https://steamcommunity.com/id/Psych0Spip
En regardant les anciens pseudo on peut voir le vrai nom de PsychOspip:




Le flag est: Josip Dvořáková

#TeamFLS-3
Énoncé :
Qui est RedScr4t ?
Solution :
Nous avons vu que Josip Dvořáková fait partie des FLS, son père est le propriétaire du site
https://pokrocilymedicinskysystem.cz. En analysant ce site web avec l’outil web-check.xyz, nous
trouvons la trace d’un fichier https://pokrocilymedicinskysystem.cz/.well-known/security.txt. Celui-
ci indique:
   Contact: mailto:ivankana+redscr4t@ozmail.eu
   Expires: 2026-04-30T22:00:00.000Z
   Preferred-Languages: cz



On en déduit que redscr4t est un alias pour ivankana sur cette boite mail.
Une recherche sur le pseudo ivankana avec l’outil https://usercheck.oscarzulu.org/ nous remonte
un compte bluesky https://bsky.app/profile/ivankana.bsky.social




Celui-ci appartient à Ivan Kanalchukiev
Le flag est: Ivan Kanalchukiev
#MasterMind
Énoncé :
Qui serait MasterVeverka ?
Solution : Des informations que nous avons trouvé, nous savons que AMS tente de racheter
Mediprecog, pour cela ils ont récupéré les dossiers médicaux de la famille Boutevieux via les
diagnostiques effectués chez AITOUBIB. Nous pouvons donc déduire que le commenditaire et
donc MasterVeverka serait Zoran Dvořáková, le président de Pokročilý Medicínský Systém.

Le flag est: Zoran Dvořáková

Raoul2 (le retour)
#OldLove
Énoncé:
Le passé de Raoul a refait surface...
Qui veut-il protéger en obéissant aux ordres ?
Solution : Nous recherchons les personnes avec qui Raoul était en contact par le passé (via le
Write Up de Medileak). Nous pouvons nous pencher sur Kallopée Hadrianos, sur son compte
bluesky elle y indique ne pas se sentir en sécurité.
Son autre message est également intéressant:




Toutefois elle ne semble pas être la bonne cible et fait référence à Gizem Ihanet.
Le flag est: Gizem Ihanet

#Insécurité
Énoncé :
Où Gizem a t-elle été "menacée" ?
Solution : En retournant sur le compte Strava de Gizem
(https://www.strava.com/athletes/135688719) trouvé lors de Medileak, nous pouvons y voir de
nouvelles courses. Une des courses est intéressant, elle y indique avoir subi une agression le
24/04/25.
Le flag est: 35.1666, 32.6731

#Mission
Énoncé :
Où Raoul doit-il "frapper" ?
Solution : Un message sur la webradio lavoixdeleurope attire notre attention, elle y indique un
message spéciale pour R (que nous supposons ici être Raoul). A première écoute on y entend
qu’une série de bruits étranges. Toutefois il s’agit véritablement d’une transmission SSTV, bien
connue des radioamateurs pour la transmission d’images fixes à l’aide d’une bande passante
réduite. En utilisant un décodeur d’image SSTV nous pouvons retrouver l’image transmise:
On reconnait ici des coordonées What3words (https://what3words.com/racleur.aviateur.vibreur)
pointant à Limoges:
Le flag est : 45.8291, 1.26617

#IA
Énoncé :
Quelle IA Raoul a utilisé pour developper son site de tracker de santé ?
Solution : Toujours sur la webradio, nous entendon une publicité pour les huiles de Docteur Revel
nous orientant vers le site web https://drrevel.onlineweb.shop.
Sur sont site, Raoul y vend des trackers
médicaux(https://drrevel.onlineweb.shop/product/reveltracker), dans la descritption de ces
derniers, on y voit un lien vers un autre site web:




Cette page nous demande un login que nous ne connaissons pas. Le code source semble
néanmoins effectivement écrit par une IA au vu du fort nombre de commentaires et de leur
structure.
Le fichier robots.txt nous donne des informations utiles:
On y voit l’existence d’un git et de répertoires cachés, on test donc l’accès à
https://healthcloud.iraoul.fr/.git/
Celui-ci nous donne l’ensemble du git utilisé pour le développement du site, on peut le parcourir
manuellement mais le plus simple reste de télécharger en local et d’ouvrir le git:




Le flag est: Deepseek-V3

#Soldes
Énoncé :
Pouvez vous identifier le produit de PMS que Raoul vend sur son site ?
Utiliser le code SHOP sur medileak2.oiw.fr
Solution : Sur le site de Raoul on y voit un objet identique à un autre vendu par PMS sur leur site:
https://drrevel.onlineweb.shop/product/reveltracker




https://pokrocilymedicinskysystem.cz/
BONUS
#Clochint
Énoncé :
Quel est le nom complet de la cloche française que l'on entend dans la publicité de l'association
des Campanistes diffusé par la radio ?
Format : Le Nom Complet d'une Cloche
Note : Ce challenge est complètement facultatif ! Note 2 : Ne cherchez pas la vraie
association, mais celle dont la publicité est diffusée sur le CTF
Solution :
Voici la méthode utilisée par nos gagnants de cette année, les Tacosint :
Via spectrogramme, on voit un gros pic en do#4 (j'ai vu après que le premier pic était le plus
important).




Vu qu'il n'y a qu'une cloche qui sonne et qu'elle est grave, j'ai cherché un peu et je suis tombé sur
la liste des bourdons de France. Je check celles en "do".
Dedans il y a la bonne qui est la première de la liste.
J'ai récupéré une vidéo pour comparer les spectres, ça ressemble beaucoup.
J'ai check d'autres en do mais elles sont trop aigues.
Parmi les plus lourdes, j'en ai check 2-3 mais ça ne collait pas la note du premier pic et pour
l'oreille j'ai demandé aux musiciens du groupe de me dire ce qu'ils en pensaient.
Flag : Françoise Marguerite du Sacré Coeur de Jésus

#Fl4G
Énoncé :
Il semblerait que Lucie et Fastitac se soient cotoyés dans le passé. Quel était le flag à trouver dans
leur petit "jeu" ?
Format : FLAG{H0_Y34H_UN_FL4G_D3_CYB3RB0Y}
Note : Ce challenge est complètement facultatif !
Solution :
Nous avons trouvé plus tôt le Github de Lucie Monlucin sous le pseudonyme LVC1-F3R.
En utilisant l’outil fournit en début de CTF (usercheck.oscarzulu.org), on peut chercher avec des
variantes du pseudonyme, en supprimant par exemple le tiret.
Une recherche avec lvc1f3r renvoie un profil sur l’instance Mastodon hébergée par Vivaldi :




Elle a peu posté sur ce profil, mais on trouve 2 posts qui nous donnent des informations :




Elle indique avoir publié un code récemment (qu’on ne trouve pas sur son Github), et une liste de
sites qui peuvent remplacer GitHub.
Un bel indice est d’ailleurs donné dans ce post où elle indique que Replit est parfait pour les CTF.
On retrouve un profil avec le même pseudo sur Replit : https://replit.com/@LVC1-F3R
Dans ce dépot, un projet ELIZA2 est d’ailleurs disponible, avec la possibilité de l’exécuter (mais
c’est inutile ici).
En consultant les logs de l’application, on peut trouver un fichier
 conversation_20250429_134709_bllls.txt qui contient le précieux sésame :




Flag : FLAG{M4G1C_W0RD_F0UND_CTF_2018}
Limoges
#END
Énoncé :
Eh bien, il semble que notre ami Raoul a une mission à remplir à Limoges le 3 juin 2025.
Si vous faites partie des 4 équipes qualifiées, vous serez donc aux premières loges pour découvrir
la suite de l'enquête.
Pour les autres, une visite à Limoges pour les 2èmes rencontres de la Cybersécurité organisé par
le Centre de Ressources Cyber s'impose non ?
Merci d'avoir participé aux épreuves de qualification de Medileak v2 !
Flag : #Limoges

OsintTracker




     Medileak_2.osintracker 201.9 KB

