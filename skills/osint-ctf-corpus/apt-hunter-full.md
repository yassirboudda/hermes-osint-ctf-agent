APT Hunter CTF – Writeup – Synoslabs

# APT Hunter CTF – Writeup

adm_synoslabs

April 29, 2024

`Reading Time: 69 minutes`

Le week-end du 27 mars 2024 a débuté le CTF APT Hunter organisé par des étudiants de l’école AIX YNOV CAMPUS.

Ce CTF consistait en un ensemble de 40 challenges qui touchaient différents domaines allant du GEOINT, au SOCMINT en passant par de l’investigation de cryptomonnaie et NFTs.

Nous avons terminé 4ème avec notre équipe "Incompetent Detectives" composée de MBAY, Kortez, Bouddah et moi-même (KrowZ).

Nous sommes également l’équipe qui a atteint le score maximum de 3000 points avec le nombre de résolution le plus élevé (avec seulement 12.77% de fail pour 87.23% de réussite)

Voici le classement des 10 meilleures équipes pour ce CTF:

Un grand merci aux organisateurs pour cet évènement de qualité avec plein de challenges différents, pour le scénario mis en place ainsi que pour leur réactivité pendant l’intégralité du CTF.

Merci également aux partenaires de cet évènement (Oscar Zulu, YNOV CAMPUS, Hack In Provence, OSINT Agency).

Un grand bravo à tous les participants et tous ceux ayant participé à ce CTF !

Il est possible que certaines erreurs se soient glissées dans les solutions pendant l’écriture de celles-ci. Si c’est le cas n’hésitez pas à m’envoyer un email ou me contacter directement sur LinkedIn pour m’en faire part.

Bonne lecture !

Summary

---

# Welcome !

## Introduction

Il s’agit ici des règles concernant le CTF afin qu’il se déroule du mieux possible.

On retiendra notamment ici que les tentatives d’intrusion et toutes les techniques actives sont proscrites (scans, brute force, etc…).

Flag:`lu et accepté`

---

# Synopsis

## Une communication inquiétante

Petit point scénario : on apprend qu’on doit identifier un groupe APT (Advanced Persistent Threat) pour déjouer leurs plans.

Flag:`compris`

---

# Le point d’entrée

## La lettre

Premier vrai challenge de ce CTF. Une lettre sous format texte nous est fournie. Voici ce qu’elle contient :

Si vous faites régulièrement des CTFs liés à la cybersécurité, il est facile d’identifier à quoi correspond cette chaîne de caractères qui semble chiffrée ou encodée.

Les signes`==`à la fin nous donnent un gros indice.

Si on n’a aucune idée de ce que cela peut être, il nous faut utiliser un outil pour identifier cette chaîne de caractères.

Par exemple, le site hashes.com permet de faire ça :

Il s’agit apparemment de base64. Pour en être sûr, on va utiliser CyberChef qui est un outil très puissant pour faire des convertions dans plein de bases différentes (et pas que):

On se retrouve alors en sortie avec un texte en clair, lisible que voici :

Bonjour,

Cela fait un moment que nous ne nous sommes pas rencontrés. À cette époque, vous n’aviez pas encore intégré les services de renseignements français. Les oiseaux chantaient, les voitures sillonnaient les routes, le ciel était bleu, la vie était belle…

Malheureusement, ces temps sont révolus. Je viens vers vous car la France court un grand danger. J’ai eu vent d’une information inquiétante, indiquant qu’un organisme clandestin tente de semer la terreur.

Je ne sais pas ce qui se cache derrière tout cela, ni quand cela va arriver. Cependant, j’ai réussi à intercepter un pseudonyme : _Tr0tsk1. Malheureusement, je ne peux pas mener l’enquête, car mon identité est connue.

Je vous confie donc la lourde responsabilité de découvrir la vérité et de venir à bout de cette menace. Je sais que vous avez toutes les qualités requises pour mener à bien cette mission.

Bonne chance.

B.

Après une simple lecture, on identifie un pseudo à l’intérieur :`_Tr0tsk1` Il s’agit de notre flag.

Flag:`_Tr0tsk1`

---

## Une inattention ?

A partir du pseudo trouvé dans le challenge précédent, nous devons identifier le nom et prénom d’une personne.

On va donc essayer de pivoter à partir de ce pseudo.

Un outil formidable qui nous a beaucoup été utile pendant ce CTF s’appelle whatsmyname. Il s’agit d’un outil qui va automatiser la recherche d’un pseudo sur des centaines de sites différents et nous renvoyer les résultats positifs (parfois des faux positifs et parfois rien n’est remonté alors que la page existe réellement) :

Bingo ! Un compte Twitter est identifié. Allons y jeter un oeil :

Nous avons un prénom, manque le nom. Si on descend un peu dans la liste des tweets postés par ce compte, on peut y voir quelque chose de vraiment très intéressant :

Il s’agit de son CV!

On obtient alors son nom et prénom.

Flag:`Andrejew Vladlen`

---

## La piste de l’emploi

Nous devons trouver le nom de sa dernière entreprise. Comme nous avons son CV, il suffit de le lire. On trouve Ribius:

Mais avant de valider le flag, on va quand même vérifier l’information. Heureusement, nous avons également trouvé un compte LinkedIn. Vu que nous avons son nom et prénom, LinkedIn semblait être l’un des premiers réseaux sur lequel le rechercher. Et nous l’avons trouvé : LinkedIn Andrejew

Une simple recherche Google sur son nom et prénom fonctionne également :

Sur son LinkedIn on accède à ses expériences et on peut donc s’assurer que sa dernière entreprise est bien Rubius

Flag:`Rubius`

---

## Coding

En général, les développeurs partagent leurs codes sur Github. Mais pas que, et il ne faut pas tomber dans le piège du "guessing" ou de l’intuition. Ici il nous faut des éléments concrets qui permettent d’affirmer ou d’infirmer certaines hypothèses.

Si on repart de son compte LinkedIn, dans ses activités récentes, il partage un lien vers Pastebin:

C’est donc sur ce site qu’il a publié son code.

Flag:`Pastebin`

---

## 🐍

Le code partagé via le pastebin est un programme Python du jeu de la roulette russe. On ne peut rien en tirer en tant que tel mais à la fin du programme un commentaire intéressant nous indique un lien vers un Google Drive:

En arrivant sur ce Drive, on voit le nom du fichier qui contient exactement le même code Python que celui sur Pastebin :

Flag:`russian_roulette.py`

---

## Petite baie

Encore une fois, à partir d’ici nous devons trouver un nouveau pseudo. Mais nous n’avons pas plus d’information.

Nous avons cependant accès à un Google Drive avec différents documents, une vidéo ainsi qu’une photo.

On va essayer de les analyser un à un pour essayer de ressortir de l’information pertinente et pourquoi pas les combiner pour retrouver un nouveau pseudo.

Commençons dans l’ordre. Le tout premier élément est un dossier nommé важно (qui signifie "important") et qui lui même contient un autre fichier nommé очень важно ("très important") :

Cette chaîne de caractère ressemble une nouvelle fois à du base64. On va donc essayer de la décoder avec CyberChef:

On a pour résultat un lien bitly. Dans notre cas nous sommes dans le cadre d’un CTF donc aucune raison de se méfier de ce lien mais dans un cas réel, il ne faut jamais directement cliquer sur un lien dont on ne connait pas la destination.

Petite astuce donc : avec bitly, si on ajoute un`+`à la fin de l’URL, on obtient des informations supplémentaires concernant la redirection ainsi que sa date de création :

Grâce à nos compétences d’OSINT, nous venons d’éviter un Rickroll 😎

Attention cependant, cette technique ne nous donne que la première redirection. Il faut alors utiliser des outils plus sophistiqués comme Lookyloo afin d’avoir une vue sur l’ensemble de la chaîne des redirections.

Il n’y a rien d’autre à ajouter sur ce document et ce dossier, il s’agissait d’une fausse piste.

Notre prochain élément est une vidéo d’une dance russe prise à partir de cette vidéo disponible sur Youtube.

En soit rien de bien intéressant au niveau du son ou du fond de la vidéo, si ce n’est qu’à un certain moment on voit passer une image subliminale qui est en fait un bout de texte :

Il apparaît à exactement 0:41 de la vidéo et on peut y extraire la chaîne suivante :

Mn6nDpQYbb6?usp=sharing

Cela ressemble fortement à la fin d’un lien de partage d’un document ou d’un drive Google. Malheureusement, l’URL est bien trop courte pour l’instant pour pouvoir faire quoi que ce soit. Mais on le garde quand même de côté.

Vient ensuite le fichier russian_roulette.py contenant le programme Python qui ne nous est pas utile.

Une photo du kremlin est postée sur le drive. Elle est nommée kremlin.png.

On va donner la photo à Aperisolve qui est un site web (également disponible en local via une installation Github) qui va prendre en entrée une image/photo et qui va lancer sur celle-ci une batterie d’outils de stéganographie afin d’automatiser la tâche et nous ressortir des informations pertinentes (ou pas).

Dans tous les résultats, la partie avec l’outil Zsteg nous intéresse parce qu’elle contient une chaîne de caractères qui a l’air de ressemble à une partie d’une URL en lien avec Google Drive (en particulier avec le "folders") :

On le note bien précieusement et on le garde de côté pour la suite :

folders/1eXT8Wxae6qgH52AkYmUvT

Le tout dernier document s’intitule document.docx et contient beaucoup de texte en russe. Nous l’avons traduit sur Deepl, et en regardant le résultat nous avons trouvé quelque chose d’étrange :

En plein milieu du texte, on retrouve le début d’un lien Google Drive. Sauf que nous ne l’avions pas vu au premier coup d’oeil sur le document original. Pourquoi ? Tout simplement parce que ce texte avait été caché en étant écrit en blanc sur fond blanc.

En sélectionnant l’intégralité du document sur Google Docs, on voit bien ce lien apparaître :

Cela nous confirme qu’on cherche bien un lien en rapport avec Google Drive. Nous avons toutes les parties à notre disposition pour les assembler et créer un nouveau lien :

- https://drive.google.com/drive/: trouvé dans le document word écrit en blanc sur blanc.
- folders/1eXT8Wxae6qgH52AkYmUvT : trouvé via Aperisolve dans les données ressorties par Zsteg
- Mn6nDpQYbb6?usp=sharing : trouvé en plein milieu de la vidéo sur le Drive.

Nouveau lien : https://drive.google.com/drive/folders/1eXT8Wxae6qgH52AkYmUvTMn6nDpQYbb6?usp=sharing

On accède alors à un nouveau drive :

Le nom du drive est Мой диск qui signifie "Mon drive". Il ne contient qu’un seul dossier nommé test qui lui même contient un document Удалить ("Supprimer") :

Il s’agit d’un organigramme dont on identifie un nouveau pseudo qui est celui qu’on cherche !

Flag:`K4m3n3v`

---

# L’escalade d’un hacker

## Here comes a new challenger

Lors du challenge précédent nous avons obtenu un nouveau pseudo : K4m3n3v Il faut désormais trouver un post de quelqu’un qui se plaint de lui.

Après avoir essayé différents réseaux sociaux comme Twitter, Instagram, Bluesky, c’est sur Facebook qu’on va trouver ce qu’on cherche avec ce post:

Nous avons recherché directement sur le réseau social car rien n’est remonté via Google

Le compte Facebook qui se plaint de K4m3n3v est un certain Julien Prevot. Attention au format du flag, ici on le veut sous la forme Nom Prénom

Flag:`Prevot Julien`

---

## You have been h4ck3d !

Ce challenge nous parle d’un "défacement" et ça tombe bien puisque c’est l’objet du poste de Julien Prevot à ce sujet (voir challenge précédent). Cependant nous n’avons qu’une capture d’écran et aucun lien qui pourrait nous rediriger vesr le site en question.

Si on se rend sur son profile Facebook on peut voir un autre poste qui parle d’un site : https://sea-cipher.fr

Julien Prevot est également CTO chez l’entreprise du même nom que le site comme en témoigne son poste renseigné directement sur Facebook :

Une fois arrivé sur le site on voit bien qu’il a été "deface". Le nom du groupe est affiché en grand sur la page :

Flag:`KolymaByte`

---

## Infiltration Virtuelle

Notre investigation se déroule désormais sur le site web de Sea Cipher. Il a été deface et notre objectif est de trouver le point d’entrée ainsi que le nom du programme utilisé par le pirate afin de compromettre le système.

On se souvient de la règle du CTF de ne pas faire d’actif sous forme de brute force, fuzzing et autres joyeusetés.

L’un des premiers réflexes à avoir sur un site web est de vérifier si celui-ci possède un fichier nommé`robots.txt`à sa racine. Cette page sous forme de fichier texte permet de définir des chemins à certaines pages du site qui ne doivent pas être indexées par certains moteurs de recherche. En effet, Google, Bing et les autres moteurs de recherche possèdent des "robots" qui vont aller scrapper les différents sites sur Internet afin d’indexer les différents contenus sur les moteurs de recherche respectifs.

Afin de contrer ça, on peut spécifier dans ce fichier`robots.txt` les pages qui ne doivent pas être indexeés.

Cela a un avantage pour nous puisqu’on y apprend l’existence de certains dossiers :

Aucun n’existe sur le site sauf /backd00r/. On y accède alors et on tombe sur cette page :

C’est la backdoor utilisée par les attaquants pour pouvoir deface le site.

Le nom du programme est spécifié tout en haut.

Flag:`WebShellUploadV3`

---

## Update your system !

Concernant la version de PHP, rien de plus simple, elle est également spécifiée sur la même page que le challenge précédent sur le site : https://sea-cipher.fr/backd00r/:

Flag:`4.3.2`

---

## Crypto

Dans ce challenge, on nous demande le cours du SeaCipher en fin mars 2024. Au moment du challenge nous sommes en avril donc la date est déjà passée depuis plusieurs semaines. De plus le site est deface et nous n’avons plus accès aux données qui étaient présentes sur le site avant cet évènement.

Et pour retrouver ça, nous avons notre ami the Wayback Machine !

Sur ce lien on peut voir qu’il n’y a que deux captures pour le mois de mars. On veut celle fin mars donc en date du 25 mars :

Une fois sur l’archive on identifie le prix du SeaCipher de l’époque :

Flag:`0.0000000035`

---

## Signature

Pour connaître l’autre nom du hacker, il faut continuer de fouiller le site web à la recherche de quelque chose qui pourrait ressembler à une signature.

Si on regarde le code source de la page qui contient la backdoor (https://sea-cipher.fr/backd00r/), on obtient ceci :

Il s’agit du pseudo de base de la personne mais inversé et en ayant rajouté des underscores au début et à la fin.

Flag:`_v3n3m4K_`

---

# Un projet ambitieux

## L’entreprise sous attaque

Nous cherchons le nom d’une entreprise qui est particulièrement ciblée par ce hacker.

Nous avons un nouveau pseudo (_v3n3m4K_) par rapport au challenge précédent donc nous allons tenter de pivoter dessus. Pour se faire, nous allons encore utiliser le site WhatsMyName:

On trouve un compte Mastodon associé avec des informations pertinentes :

1. Взломай мир veut dire "Hack the world"
2. Профиль в рамках соревнования CTF veut dire "Profile within the CTF competition"
3. Приветствую сообщество, знакомо вам KolymaByte? Они недавно ко мне обратились… veut dire "Hello community, are you familiar with KolymaByte? They recently contacted me…"

Et tout en haut dans la description, un lien qui redirige vers un compte Github : https://github.com/k4menev/

Seul le dernier repository nous intéresse parce que c’est le seul qui est créé par la personne. Le reste ne sont que des forks (des copies).

Le code sur ce repo correspond à un reverse shell écrit en C. Mais qui dit reverse shell, dit obligatoirement une adresse ou une IP précisée pour que le shell puisse venir se connecter à un C2. Or ici, la seule chose qui est spécifiée est ‘target_website’ comme si la chaîne de caractère de base avait été remplacée.

Pour être sûr on peut regarder les anciens commits du repo Github pour voir toutes les modifications effectuées au code via Github :

On accède alors à l’historique. Il y en a deux. On peut aller voir les modifications faites pour la dernière version en date (celle qu’on voit actuellement sur le Github) :

On se retrouve alors avec les éléments modifiés d’une version à l’autre, dont le nom de l’entreprise visée par cette attaque :

Flag:`Stella Launch Solutions`

---

## Mise en orbite

Nous avons un nom d’entreprise mais également un lien direct vers le site web comme trouvé dans le challenge précédent :`stella-launch-solutions.com`

On va donc essayer de voir sur ce site si on ne peut pas trouver des informations sur les membres de l’équipe et ainsi identifier le ou la responsable de la section R&D.

Effectivement, dans la section liée aux membres de l’équipe on retrouve une certaine Matilda Beck qui est "R&D Division Manager" et donc responsable.

Flag:`Matilda Beck`

---

## Énigmes des ondes

Lors de ce challenge, deux captures d’écran nous sont données. Les voici :

Il s’agit de deux conversations différentes entre personnes dont on ne connaît pas encore le nom, ni le pseudo et encore moins les motivations.

Voici la traduction de la conversation de droite qui est écrite en chinois :

Notre but ici est d’identifier un nouveau pseudo. Le seul pseudo qui ressort des deux conversations est Dux1u.

Flag:`Dux1u`

---

## Un bon ami

Si on repart des captures d’écran du challenge précédent, nous n’avons rien ressorti du screenshot de droite en chinois.

Pour celui de gauche on sait que la personne qui a pris les captures d’écran est`Dux1u` lui même puisque les messages sont en vert de son côté et que c’est`K4m3n3v` qui l’appelle`Dux1u`.

Ils s’appellent par leurs pseudos donc ne semblent pas amis.

Par contre avec l’autre personne, on connait directement son prénom (en haut de la conversation). Il s’agit de Zhijang. De plus il a l’air de vouloir se confier à lui, ce qui nous conforte dans l’idée qu’ils ont un lien d’amitié.

Flag:`Zhijang`

---

## L’Identité Révélée

Nous devons identifier la véritable identité de`Dux1u`.

Pour cela, nous allons de nouveau nous baser sur les conversations présentées dans les deux challenges précédents.

Dans la première capture on y apprend que`Dux1u` a été viré de l’entreprise sans aucune raison et qu’il souhaite se venger.

Jusqu’ici ça colle avec toutes les informations récoltées jusqu’à présent : reverse shell, deface par K4m3n3v avec qui il est en contact.

S’il faisait partie de l’équipe de Stella Launch Solutions peut-être qu’il était également présent sur le site web de l’entreprise ? Pour vérifier on utilise une nouvelle fois la Wayback Machine pour essayer d’identifier qui est la personne qui était présente à l’époque et qui ne l’est désormais plus :

C’est la seule personne qui n’est plus représentée sur la version actuelle du site de Stella Launch Solutions

Flag:`Wen Ch'ien`

---

## Entrée secrète

On apprend ici qu’apparemment une autre backdoor est présente sur le site de Stella Launch Solutions. On tente de nouveau les mêmes techniques, notamment avec le`robots.txt` mais rien n’est retourné.

Nous avons alors cherché sur Google en tapant le nom de l’entreprise et nous avons trouvé des scans qui ont été fait sur le site afin d’identifier de potentielles URLs cachées :

On y voit une URL qui a l’air d’avoir été construite pour être cachée ainsi qu’un screenshot associé à la page qui ne ressemble pas du tout au site web de Stella Launch Solutions :

En se rendant directement sur l’URL on tombe sur un shell sur lequel on peut exécuter certaines commandes :

Le nom du programme est spécifié tout en haut de la page.

Flag:`ReverseShellWebV1.1`

---

## Command and Control

En tapant la commande`help`, il nous est possible de lister toutes les autres commandes possibles. On va donc les exécuter une à une et regarder ce qui ressort :

Énormément d’informations ont l’air pertinentes. On garde bien en tête toutes les données sur cette capture d’écran pour les futurs challenges.

Mais en attendant on va se contenter de répondre à la question de celui-ci. Le deuxième encadré rouge correspond à la version de l’agent déployé sur la victime.

Flag:`1.1.3`

---

## Trafic dissimulé

Dans le précédent challenge, nous avions vu qu’il y avait beaucoup d’informations ressorties du webshell, dont une étrange chaîne de caractères vraiment longue qui est la suivante :

```
Dzt(X*bSyiGHq+43GHv*kG4Rygp^+kjVE^=RrF+f@Rt0C0^=DYk+kA6}JNF#jw^8HgkpTt5Wt)qCB
```

C’est censé être un nom d’hôte mais cela ne ressemble pas du tout à quelque chose de lisible. Il doit donc y avoir une obfuscation.

Il y a des caractères spéciaux (`^@})*`) donc ça ne peut pas être un hash (normalement on aurait que de l’hexadécimal).

Si on tente tous les outils d’analyse de hashs possibles, aucun ne nous renvoie quelque chose de pertinent.

Je vais pas vous mentir, ici c’est surtout grâce à mes précédentes expériences de CTF en cybersécurité que j’ai tout de suite pensé à de l’encoding dans une base très élevée. Pourquoi ? Parce qu’en base64 on utilise 64 caractères différents pour encoder l’information (26 minuscles + 26 majuscules + 10 chiffres + 2 symboles (`+/`)).

Ici on en a beaucoup plus et donc ça ressemble à une base beaucoup plus élevée. Si on regarde sur CyberChef:

On peut aller jusqu’à la base92, donc 92 caractères utilisés pour encoder l’information.

On tente les différentes bases et on se retrouve avec ce résultat :

Le base92 fonctionne et nous renvoie une adresse en .onion

Flag:`co4fuiol57xfwjobszioknloyqejrxr7emsey5obnhsnwg23725jn6yd.onion`

---

# Un bon plan financier

## Revente

On repart du pivot qu’on a trouvé pour le challenge précédent (le site en .onion) et on y accède en utilisant Tor Browser (ou Brave ou peu importe tant qu’on est connecté au réseau Tor) :

Il s’agit d’une plateforme comme on peut en trouver pour les groupes de ransomware qui mettent en vente les données des entreprises compromises. Dans le lot des entreprises, on retrouve celle qu’on cherche :

Flag:`6.997`

---

## Monnaie virtuelle

Le site possède plusieurs onglets :

- Celui de base sur lequel on arrive et contient la liste des données d’entresprises à acheter.
- Un autre qui contient les instructions afin d’effectuer les paiements : http://co4fuiol57xfwjobszioknloyqejrxr7emsey5obnhsnwg23725jn6yd.onion/how-to-buy.html

On y retrouve l’adresse du wallet sur laquelle envoyer de l’argent :

Flag:`0xCec4748becc7eC74214cA0BDb3bC8DDAf68D4108`

---

## Achat

Maintenant que nous avons un wallet, il faut l’investiguer. La première chose à faire est d’identifier la blockchain.

Une rapide recherche sur Google nous donne le nom de celle-ci :

Il s’agit de Sepolia. C’est une blockchain de "test" qui utilise de la fausse monnaie qui n’a pas réellement de valeur (parfait dans le cadre d’un CTF).

Maintenant il faut connaître ce qu’on cherche. On veut essayer de trouver une transaction liée aux données de l’entreprise "Gourmet Brasserie".

Sur le site des pirates, on retrouve le prix de ces données :

On se doute que dans les transactions on va devoir chercher une trace de ce même prix.

On se rend alors sur Etherscan qui nous permet de librement naviguer sur la blockchain et trouver des informations sur les wallets, transactiopns, NFTs, etc…

Dans toute la liste des transactions pour cette adresse, on en retrouve bien une qui a l’air de correspondre :

On peut aller sur cette adresse pour vérifier qu’il y a bien une transaction en sortie pour celle-ci : https://sepolia.etherscan.io/address/0xee70bde4bc29f2491b8aef671298e0ba73d3ef52

Flag:`0xee70bde4bc29f2491b8aef671298e0ba73d3ef52`

---

## La clé financière

On cherche ici le pseudo d’une personne en charge de la trésorerie. Apparemment un détail doit nous intriguer par rapport à ça.

La première chose qu’on trouve réellement bizarre est la boucle des transactions entre trois adresses distinctes :

L’adresse de base des pirates (`0xCec4748becc7eC74214cA0BDb3bC8DDAf68D4108`) envoie`2.42354676 ETH` sur cette adresse :`0x0D1C7d776693d76cc974B9c06d3c6B543faC36C4`.

Cette même adresse renvoie`1.5 ETH`à une nouvelle adresse`0xff374A42f5FAFd8120269adE26c1F09A318aa200` qui elle-même renvoie de nouveau`1.4240613 ETH`à l’adresse des attaquants :`0xCec4748becc7eC74214cA0BDb3bC8DDAf68D4108`

Pour simplifier, voici un magnifique schéma :

Peut-être est-ce fait pour brouiller les pistes ? En tout cas il s’agit peut-être d’une piste donc on garde de côté et on va se concentrer sur autre chose.

Les trois premières transactions sur le wallet (les plus anciennes) concernent des achats de données. Sur le site il y a également trois entreprises dont les données on été achetées et sont donc barrées. Ce qui confirme cette hypothèse :

Avec également "Продано" en russe qui pourrait se traduire par "acheté".

Si on se renseigne un peu plus sur ces adresses de wallet, on remarque que deux d’entre eux possèdes des NFTs :

- `0xee70bdE4Bc29F2491b8aeF671298E0bA73D3eF52`
- `0xcD5e107b4A3884dA16db5ef4f73d48954f60d6ff`

On voit ici avec par exemple la première adresse : https://sepolia.etherscan.io/address/0xee70bde4bc29f2491b8aef671298e0ba73d3ef52

On peut lister les items : https://sepolia.etherscan.io/address/0xee70bde4bc29f2491b8aef671298e0ba73d3ef52#nfttransfers

Et on voit également au niveau de la transaction de ce NFT qu’il y a une données qui a été ajoutée : https://sepolia.etherscan.io/tx/0x4f57753eb4e2e82f1f1eae6b34da2fcad9732820d587fbdca588b138c51b17cd

Il s’agit d’un lien vers du stockage sur le cloud : https://nftstorage.link/ipfs/bafybeiagcwda4u32yofiyguzudlmydxuwlomuryvbbecjaugrlfj44ssaa/696a9f4b-da39-44e0-bc21-5b6c537ad7c1.json

Il semble s’agir d’un fichier PDF, voyons à quoi il correspond : https://bafybeia4b5h7h4glrfq2ylxxlhffdxpz6rptrsf5m7uzz2c2cqiygrj3qy.ipfs.nftstorage.link/invoice-01236.pdf

C’est une facture numérotée invoice-01236.pdf qui confirme l’achat des données par la personne possédant le wallet`0xee70bdE4Bc29F2491b8aeF671298E0bA73D3eF52` vers`0xCec4748becc7eC74214cA0BDb3bC8DDAf68D4108`

Chose étrange on y retrouve une note qui n’a aucun sens et qui n’a rien à faire là. Et c’est "signé" avec un`#AU`.

Nous avons cherché sur Internet au niveau du logo utilisé sur la facture pour potentiellement identifier une entreprise. Mais il s’agit simplement d’un logo Freepik :

Pour l’instant on met ça de côté. Mais qui dit une facture pour une transaction veut peut-être dire d’autres factures pour les autres achats de données.

On avait identifié deux wallets qui possédaient des NFTs. Voici le deuxième qui lui en possède trois : https://sepolia.etherscan.io/address/0xcd5e107b4a3884da16db5ef4f73d48954f60d6ff#nfttransfers

On ne va pas détailler de nouveau les mêmes étapes pour retrouver les transactions ainsi que les factures mais voici une liste exhaustive de tous les liens pour que vous puissiez vous y retrouver plus facilement :

Première transaction de NFT : https://sepolia.etherscan.io/tx/0x6675c8c349d327748c06ff9ac547d999e7c4226adc5e81d3ccdf6d470004299e qui redirige vers le stockage https://nftstorage.link/ipfs/bafybeidagz3pdv5e3twagls6w5imobeqvg2qvhxbjecovv7axwlf5a3sxq/5b66107a-6baf-4f48-932b-ed295f1f47c4.json qui contient la facture`invoice-01234.pdf`: https://bafybeicyq2d54k3nzcrysjja2xnltanuotsdhrgo7tba352goh75gzoe5a.ipfs.nftstorage.link/invoice-01234.pdf

Seconde transaction de NFT : https://sepolia.etherscan.io/tx/0xf0dc112e846a762cc61b95382c4a7d2520495df1961757f4b851ecd3f4bc30ea qui redirige vers le stockage https://nftstorage.link/ipfs/bafybeicrzmtvergh5dedb3dtnkdq5svbr2dunlidodrsl26iy742fm7equ/f8209d17-6cae-44f6-aad0-75debbca2f37.json qui contient la facture`invoice-01235.pdf`: https://bafybeiexbfgp2ea3cgrblptdxao3iga4feea46xol2vzi7sshdl5rh5wsi.ipfs.nftstorage.link/invoice-01235.pdf

Troisième transaction de NFT : https://sepolia.etherscan.io/tx/0x636a51b417c4c7cdee845f3d262bc3f15010b612824c07e65e0074aa9fcd845a qui redirige vers le stockage https://nftstorage.link/ipfs/bafybeiepduvut3vq6m6eo6tjnytajycuwaxq4kglcyhnrmq6xrrrmy63fa/0698053c-7cb8-4041-afb4-23530c5b4fe4.json qui contient cette fois-ci non pas une facture, mais une lettre ! https://bafybeihgxar7cuhiu255fkequ2jfnw4y77uigmfzcwtnonn53xzqxvureu.ipfs.nftstorage.link/borxhit.jpg

Cette dernière est aprticulièrement intéressante parce qu’on en apprend plus sur un wallet et sur l’acheteur d’une des données :

Cette note en tant que telle ne sert à rien pour le challenge mais nous donne un meilleur contexte au niveau du scénario. Il y a d’ailleurs une référence à un précédent CTF de la team Oscar Zulu puisque la personne qui demande un prêt s’appelle Gérard Dakarivitch qui était un personnage fictif utilisé pour les CTF "Disparue(s)".

Autre point assez étrange qui nous a perturbé pendant ce challenge concerne la facture numéro`INV-01234`. Dans celle-ci, c’est l’adresse des attaquants qui envoie de l’argent vers une autre adresse pour l’achat de leurs propres données. Ça n’a aucun sens d’acheter ses propres données. Nous avons alors penser que cela pouvait être du blanchiment d’argent ou bien qu’ils ont acheté leurs propres données pour faire croire que leur service était fiable et qu’ils avaient déjà des clients.

Il s’est finalement avéré qu’il s’agissait simplement d’une petite erreur des organisateurs lorsqu’ils ont généré le PDF.

Donc pour l’instant la seule piste viable que nous avons sont les notes étranges qui ressembent à des parties de poèmes à chaque fin de facture. Toutes signées par`#AU`.

Nous avons essayé de chercher sur les principaux réseaux sociaux comme Facebook, Instagram, Twitter mais rien ne remontait. A la fois en utilisant des dorks sur les notes mais aussi le hashtag.

Comme énormément d’équipes étaient bloquées à cette étape, les organisateurs ont décidé de tous nous donner un petit hint :

On reconnait directement la mascotte du réseau social Mastodon.

Nous nous sommes donc précipités sur celui-ci afin de trouver ce qu’on cherchait. Après de longues minutes de scrolling, dans la partie hashtage on trouve une citation qui nous est familière : https://mastodon.social/tags/au

On a déjà dû scroll (beaucoup trop) pour arriver jusqu’à ses postes. Imaginez seulement au moins une semaine après lors de la rédaction de ce writeup :'(

Flag:`Arina_Uvrv`

---

## La Traque Financière

Nous avons un pseudo ainsi qu’un nouveau réseau social. Il est tant de découvrir la véritable identité derrière cette trésorière d’un groupe de hackers.

En cherchant un peu plus en profondeur sur son profil Mastodon, on trouve ce message qui nous met la puce à l’oreille : https://mastodon.social/@Arina_Uvrv/112231020105419499

En regardant la tout première version du message on y trouve un pseudo qui a l’air de pointer vers Tumblr :

On y trouve effectivement son profil sur cette plateforme, ainsi que sa vraie identité : https://www.tumblr.com/a–uvarova

/!\ Attention au format du flag qui est "Nom Prénom"

Flag:`Uvarova Arina`

---

# Un bol d’air

## Sous le ciel d’adieu

Sur son Tumblr, Arina a posté plusieurs photos de ses différents voyages. Notamment une qui a l’air de ressembler à un aéroport : https://www.tumblr.com/a–uvarova/746653119764725760/sous-le-ciel-dadieu-mes-pas-vers-lavant-se

Il y a un poème en dessous mais nous ne nous en sommes pas servi.

Notre but est donc de retrouver le code OACI de l’aéroport en question qu’on voit sur la photo. Un code OACI est simplement un identifiant unique que possède chaque aéroport dans le monde.

On fait une première tentative de géolocalisation en utilisant bêtement Google Lens :

Malheureusement les résultats ne sont pas concluant et Lens nous ressort plutôt des images de bateaux.

Nous avons donc décidé de faire appel à l’IA (https://remini.ai/) pour essayer de rendre la photo un peu plus nette :

Après un essaie infructueux, on retente avec cette nouvelle image générée et on tombe sur quelque chose qui pourrait correspondre :

Si on clique sur le lien, nous arrivons sur un site russe qu’on va s’empresser traduire : https://www.aex.ru/news/2023/3/13/254665/

Il s’agirait de l’aéroport de Surgut.

On confirme et vérifie ensuite l’information en se rendant directement sur Google Street View pour essayer de trouver un point qui ressemble "surgut airport": https://www.google.com/maps/@61.3405439,73.4064722,3a,19.5y,92.07h,93.42t/data=!3m8!1e1!3m6!1sAF1QipOsoCgOgbsvQxdI5jpDM5tHcICfseqOtzUFeb0V!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipOsoCgOgbsvQxdI5jpDM5tHcICfseqOtzUFeb0V%3Dw203-h100-k-no-pi-0-ya295.2383-ro-0-fo100!7i8704!8i4352?entry=ttu

On trouve finalement le code OACI :

Ce qu’on peut retenir cependant c’est qu’une image très légèrement modifiée dans Google Lens peut donner des résultats étonnement différents. De même si on utilise une même image mais qu’on ne la cadre pas de la même façon. Il faut donc parfois essayer plein de vues différentes et "brute forcer" l’outil pour trouver quelque chose de pertinent.

Flag:`USSR`

---

## Un bon bol d’air

Pour ce challenge on retourne sur le profil Mastodon d’Arina et on se dirige cette fois-ci vers une autre photo qui a été prise le 4 avril 2024 et qui montre une belle vue sur un lac : https://mastodon.social/@Arina_Uvrv/112212180236514148

Une nouvelle fois un Google Lens dessus nous donne le lieu :

Il s’agit d’Harder Kulm situé en Suisse.

La partie difficile est de réussir à savoir dans quelle ville est situé ce fameux "Harder Kulm" car il y a plusieurs possibilité et les différents sites consultés ne nous donnent pas tous la même information :

Si on regarde les différents villes proche sur Maps, c’est Unterseen qui a l’air de correspondre puisque l’agglomération englobe Harder Kulm :

Flag:`Unterseen`

---

## Un abri temporaire

On nous parle d’une photo ainsi qu’une résidence et d’une année présente sur la façade de l’établissement.

On switch de nouveau sur le profile Tumblr d’Arina pour ce challenge : https://www.tumblr.com/a–uvarova/746818709675524096/ce-pays-mavait-manqu%C3%A9-ma-bonne-action-du-jour

On a une idée du lieu où elle se situe.

Une petite recherche Google Maps nous donne la réponse :

Mais en confirme quand même la localisation pour être certain de ce qu’on avance :

Même si nous ne sommes pas exactement au même endroit, il s’agit du même lieu qu’on voit en fond sur la photo. Elle n’est sûrement pas exactement dans le restaurant de Barry parce qu’elle nous indique ce soir qu’elle y est invitée.

Sur son tout dernier poste on voit ceci : https://www.tumblr.com/a–uvarova/747049100250431488/heureusement-que-jai-une-belle-vue-depuis-ma

Il nous suffit alors de former un rayon de 100 mètres autour du restaurant de Barry pour trouver les potentielles résidences. Autre chose importante dans le texte : on y apprend qu’il y a un bar juste en face de la résidence, ce qui réduit considérablement les possibilités.

Grâce à Google Earth on va tracer cette délimitation avec l’outil "cercle" :

Ce qui nous donne à peu près cette zone (à +- 10 mètres près).

Si on se promène un peu sur la route principale vers l’est, on tombe sur cet hôtel juste en face d’un bar (en rouge sur la capture) et qui possède une date sur sa façade :

On confirme puisque la distance par rapport au restaurant de Barry est d’environ 100 mètres comme ideniqué dans le post de base :

Flag:`1843`

---

# Le temps presse..

## Mise au point

Nous repartons tout au début de l’enquête avec la première personne que nous avions identifiée : Andrejew Vladlen

On doit maintenant découvrir où il habite.

On se souvient qu’il avait un compte Twitter ainsi qu’un CV. On avait aussi trouvé son compte LinkedIn afin de vérifier sa dernière entreprise mais s’était arrêté ici.

On va revenir sur son compte LinkedIn pour identifier un post qui paraît fort intéressant et qui nous donne énormément d’indices :

On sait déjà qu’il vit désormais en France comme indiqué dans sa localisation LinkedIn :

Le hashtag`#cybersecuritycity` est également un gros indice puisque la ville par excellence en France qui représente le mieux la cybersécurité est Rennes.

On aurait pu utiliser des outils comme Overpass Turbo afin de trouver les éléments essentiels à notre recherche mais nous avions tellement d’informations dans ce texte que nous avons choisi de "brute force" les possibilités.

Déjà on sait qu’il y a des cloches à proximité. Donc on va regarder de ce côté pour commencer :

Tout nous renvoie vers la cathédrale Saint-Pierre :

Il nous suffit de trouver une crêperie ainsi qu’une fleuriste proche de ce lieu :

On a principalement quatre possibilités.

Reste à trouver une crêperie très proche de l’un de ces points. On va commencer par le numéro un (comme par hasard) nommé "Maison Tulipe" :

Tiens donc, ne serait-ce pas une crêperie à côté d’une fleuriste dans une rue piétonne sans voiture proche des cloches dans une ville vivante, capitale de la cybersécurité en France ? (je crois que si).

Il parle de la fleuriste du rez-de-chaussée donc il est dans le même immeuble que la fleuriste :

Il s’agit du numéro 9. Cependant la fleuriste n’était pas encore présente sur Street View puisque la capture du lieu date de Juillet 2013 alors que son établissement secondaire n’a été créé qu’en 2023 : https://www.pappers.fr/entreprise/maison-tulipe-948348354

Flag:`9 rue du Chapitre, 35000 Rennes`

---

## 6h00

Pour ce challenge il nous est donné l’image suivante :

On reconnait encore une fois la signature d’Arina avec son fameux`#AU` ainsi que le "poème" qui indique :

```
Quand les nombres se révèlent,
dans la cavité de l'oreille,
les secrets s'éveillent.
```

Ça nous donne un gros indice sur le fait qu’il va très certainement falloir appeler ou au moins interagir avec ce numéro de téléphone.

Problème, il s’agit d’un numéro qui contient des caractères qui ne devraient pas faire partie de celui-ci. On y retrouve notamment deux fois la lettre "F".

Pour ceux habitués des CTFs ou qui ont déjà fait un peu de cyber et/ou réseau, on reconnait rapidement ici de la base 16, aussi appelée hexadécimal.

Au lieu de compter comme d’habitude en base 10 avec des chiffres allant de 0 à 9 (il y a bien 10 chiffres différents), en base 16 on va utiliser 16 caractères pour compter. Le problème c’est qu’il n’y a pas plus de 10 chiffres disponibles. Donc on va utiliser des lettres. "A" va correspondre à 11, "B" à 12, et ainsi de suite jusqu’à "F" = 15. De 0 à F on a donc bien 16 caractères différents.

On a fait l’erreur au début de ne convertir en base 10 que les caractères qui nous semblaient être en base 16. C’est-à-dire le 5F et 4F. C’était une erreur puisque même si "07" peut ressembler à un nombre en base 10, il peut très bien être également en base 16. Il s’écrira alors de la même manière mais ne vaudra pas la même valeur.

Si on convertit l’ensemble des nombres en base 10 on obtient :

Peu importe l’outil, ils font tous à peu près la même chose.

On se retrouve alors avec un nouveau numéro : 07 56 95 79 81

Quand on tente de l’appeler, on tombe sur une boîte vocale qui nous donne un à un des lettres sous format "alphabet militaire". C’est à dire que pour signifier "A", on va dire "Alpha", pour "B" on utilise "Bravo" et ainsi de suite.

Voici l’enregistrement vocale lorsqu’on appelle le numéro : https://synoslabs.com/wp-content/uploads/2024/05/code_otan.mp3

L’alphabet avec leur prononciation est le suivant :

Après plusieurs écoutes, on arrive à identifier toutes les lettres et à reconstruire l’URL qui nous est donnée : bit.ly/APJDROZ

Petite astuce pour les liens bit.ly : on peut ajouter un signe`+`à la fin de l’URL pour voir la prochaine redirection et connaître la date de création du lien :

Flag:`https://bit.ly/APJDROZ`

---

## La dernière pièce du puzzle

On a vu dans le précédent challenge que le lien bit.ly nous renvoyait vers un nouveau drive Proton : https://drive.proton.me/urls/7NW5S7XHKG#zsDBcgOK9YRC

On s’y rend donc et nous avons désormais quatre documents à analyser. Ici on s’en occupera que d’un seul car le reste ne nous est pas utile actuellement mais pour un futur challenge.

Celui qui nous intéresse est donc le document appelé Фото на память 😂.pdf

Ce qui signifie "Photo pour mémoire 😂.pdf".

En voici le contenu :

Au moment de l’ouverture de ce document nous connaissions quatre personnes sur les cinq. TIGRAN Zhirov était en fait le hacker K4m3n3v qui est décédé comme indiqué dans la revue de journal (un autre document du même drive dont on parlera très rapidement dans le prochain challenge mais qui n’a aucune conséquence sur le CTF, si ce n’est sur le lore).

On apprend désormais l’existence de GOLUBOV Sviatoslav qui est le leader de cette organisation.

Flag:`Golubov Sviatoslav`

---

## Lieu secret

Ce challenge est celui qui rapporte le plus de points de tout le CTF. Il n’est pas forcément très compliqué mais il faut bien suivre toutes les indications pour ne pas se perdre.

On commence par reprendre les éléments du drive sur Proton un à un pour ne rien manquer : https://drive.proton.me/urls/7NW5S7XHKG#zsDBcgOK9YRC

Le premier document est un audio sous format mp3. Il a pour titre "для пути.mp3" qui signifie "pour le chemin.mp3". C’est un gros indice sur le fait qu’il nous sera utile pour trouver les coordonnées de la planque.

Voici à quoi il ressemble : https://synoslabs.com/wp-content/uploads/2024/05/для-пути.mp3

En soit la musique n’a rien de particulier mais à certains moments on entendu des bruits parasites.

Voici les timecodes :

- 0:16
- 0:28
- 0:52
- 1:09
- 1:30
- 1:54
- 2:08
- 2:20
- 2:39

S’il y a du bruit comme ça à des espaces assez réguliers ça ne peut pas être un bug. Il y a sûrement un message encodé dans le son.

Pour se faire, nous avons utilisé Audacity qui est un outil à télécharger qui permet de faire diverses opérations sur des bandes sons et même enregistrer via son micro, etc…

Il y a même la possibilité d’ajouter un spectogramme sur une bande son pour voir si des messages sont cachés dans l’audio.

On se retrouve alors avec ceci :

On arrive très bien à identifier qu’à chaque fois qu’il y a un artefact audio au niveau du son, cela correspond à un caractère.

A la fin, on a réussi à identifier les neufs bruits qui correspondent à cette chaîne de caractères :`9JHM8CMP+`

Cela nous sera utile ensuite mais on le garde de côté pour l’instant.

Il y a également un fichier qui correspond à une image : "Статья в прессе.png" qui signifie "Article dans la presse.png"

La photo du journal ne sert à rien pour le challenge mais nous donne des indications supplémentaires concernant l’histoire du CTF et le contexte.

Vient ensuite le dernier élément qui est primordial pour résoudre ce challenge : "позволяет получить доступ к месту.txt" qui signifie "vous permet d’accéder au lieu.txt" (difficilement plus explicite) :

La traduction est la suivante :

```
À la sortie du café commence le voyage vers l'est,
Tu prendras la voiture qui t'attend,
En passant devant la réserve naturelle de la Fourmilière, un voyage infini.
Sans arrêts ni détours, exactement trente-sept kilomètres, cela continue,
Jusqu'à ce qu'un nouveau chemin se dévoile sur la droite.

Là, un pont apparaît, au-dessus de la rivière vivante,
Reconnaissable par sa clôture rouge et brillante.
Il se prolonge, emporté par le courant,
Toujours tournant vers la gauche, puis droit devant
jusqu'à ce que tu atteignes l'endroit où les gens se reposent.

À proximité, une église, là où tu pourras trouver
Une pièce de monnaie, appelle-moi lorsque tu y seras,
Nous t'attendrons au deuxième étage,
Dans le bâtiment où les balcons rouges scintillent.
```

On nous parle d’un café, très bien mais à partir de quel point doit-on partir ? C’est ici qu’entre en jeu le fameux code qu’on avait identifié avec le spectrogramme dans l’audio. Il s’agit en fait d’un code Google Maps qui pointe vers une position spécifique :

Si on zoom sur le point on trouve un café, qui correspond avec le tout début de la description du chemin à emprunter :

On sait qu’on doit prendre vers l’est comme indiqué dans la première ligne.

On doit passer à côté d’une certaine "réserve naturelle de la Fourmilière". Si on regarde aux alentours, il n’y a aucune réserve naturelle et encore moins de fourmillière. Peut-être une mauvaise traduction ?

On va tenter de faire la recherche sur Maps via le terme russe :

Effectivement, on trouve un emplacement qui a l’air d’être indiqué comme étant une sorte de réserve naturelle (point numéro 2). On a déjà le début de notre voyage.

Vient ensuite la phrase suivante :

```
Sans arrêts ni détours, exactement trente-sept kilomètres
```

On trace continue alors sur 37 kilomètres depuis notre point de départ sans prendre de sortie, tout en passant par la réserve naturelle :

On remarquera qu’on se situe juste au dessus de Surgut, ville liée au challenge "Sous le ciel d’adieu" dans lequel on devait géolocaliser l’aéroport de cette ville.

On arrive alors à un croisement. La suite des instructions sont assez claires :

```
Jusqu'à ce qu'un nouveau chemin se dévoile sur la droite.

Là, un pont apparaît, au-dessus de la rivière vivante,
Reconnaissable par sa clôture rouge et brillante.
Il se prolonge, emporté par le courant,
```

Au bout des 37 kilomètres, on prend à droite et on tombe sur une rivière :

Le pont est rouge comme indiqué :

Nous sommes toujours sur la bonne voie.

Vient à présent les deux lignes suivantes qui ne sont pas si simples :

```
Toujours tournant vers la gauche, puis droit devant
jusqu'à ce que tu atteignes l'endroit où les gens se reposent.
```

Tourner toujours à gauche, ok mais toujours à quel point ? A chaque embranchement ? En tout cas on doit arriver à un endroit "où les gens se reposent". Aux alentours il n’y a qu’une sule ville et le reste n’est que champs sans hôtel à proximité. Donc par déduction on s’y dirige :

A chaque numéro correspond une intersection et on prend à gauche à chaque fois que c’est possible.

Lorsqu’on arrive dans la ville, on tombe sur un hôpital (rouge) ainsi qu’un hôtel (rouge également). Est-ce que c’est l’hôpital qui est considéré comme un lieu de repos ou l’hôtel ? Ou les deux ?

En tout cas ça ne pose pas problème puisqu’ils sont assez proches et si on continue les instructions on confirme l’emplacement :

```
À proximité, une église, là où tu pourras trouver
Une pièce de monnaie, appelle-moi lorsque tu y seras,
Nous t'attendrons au deuxième étage,
Dans le bâtiment où les balcons rouges scintillent.
```

A proximité nous avons bien une église (jaune). Nous avons eu beaucoup de difficulté à traduire le terme "Монетка" en français. Ici dans la traduction nous avons "pièce de monnaie" mais ça a l’air de plus vouloir dire "argent". Donc vu qu’on a une banque (bleu) juste à côté ça correspond également.

On nous attend alors au deuxième étage avec des balcons rouges dans le bâtiment de la banque.

On s’y rend avec Google Street View :

Ça correspond à la description, on récupères les coordonnées GPS et on peut valider le challenge !

/!\ BONUS /!\

On a failli tomber dans un immense rabbit hole (voulu ou non par les créateurs du CTF ?) parce que le fameux mot russe qui veut dire "monnaie" est aussi littéralement le nom d’un magasin à proximité du lieu de résolution du challenge :

Et pour ne pas nous faciliter la tâche, il y a aussi des buildings en face avec des balcons rouges.

Flag:`61.600, 73.733`

---

## Opération spéciale

Un fichier texte nous est fourni avec le challenge :

Et voici la traduction correspondante :

```
Mes chers amis,

Le jour où ce satellite rencontrera notre ennemi commun entrera dans l'histoire, et nos noms seront éternellement inscrits 
dans la mémoire collective.
Je vous remercie à tous pour votre engagement dévoué dans ce projet.
Je prévois de me retirer pendant un certain temps dans un endroit secret que je préfère garder pour moi.
J'espère que vous profiterez également de ce temps pour vous.

Sans votre contribution et le soutien financier de nos partenaires, cette opération n'aurait jamais eu lieu.

Au revoir, et à bientôt je l'espère,
L3n1n3

Note pour K4m3n3v, souviens-toi, si le satellite dévie de sa trajectoire prévue et menace notre patrie,
utilise la clé d'arrêt pour tout arrêter, corrige l'orbite et relance le programme.

Si tu as oublié la clé :
Dans le nom de celui qui a construit le mausolée du leader, réside le pouvoir d'arrêter la tempête.

N'oublie pas : лук/4ec0ce6db63dd91893187c4c2348dc2c1008d6443014da4dab569e3e4d724ceb/ 
```

On cherche ici un pseudo, il n’y en a qu’un qui ressort du texte.

Flag:`L3n1n3`

---

## La tête dans les étoiles

A la toute fin de la lettre (du challenge précédent) il est mentionné :

```
N'oublie pas : лук/4ec0ce6db63dd91893187c4c2348dc2c1008d6443014da4dab569e3e4d724ceb/ 
```

Le terme`лук` signifie`onion` en anglais. On fait directement le lien avec le site onion qu’on a trouvé précédemment. On va donc y ajouter à la suite de l’URL le nouveau répertoire : http://co4fuiol57xfwjobszioknloyqejrxr7emsey5obnhsnwg23725jn6yd.onion/4ec0ce6db63dd91893187c4c2348dc2c1008d6443014da4dab569e3e4d724ceb/

On y accède et on tombe sur une nouvelle page avec un satellite et un compte à rebours qui, quand il arrivera à son terme, fera s’écraser le satellite :

Flag:`SLS1337`

---

## Arrêt net

Nous avons résolu ce challenge d’une façon qui n’était pas attendue par les administrateurs du CTF mais ça vaut quand même le coup de vous donner à la fois la manière dont on a procéder pour le réussir mais également celle qui était censée être utilisée pour arriver à nos fins.

Une fois sur la page, nous avons simplement regardé dans le code source et sommes allé sur le code Javascript correspondant au terminal.

Vu qu’il ne s’agit pas d’un vrai terminal, toutes les commandes sont émulées et écrites à l’avance. Rien n’est exécuter et on va simplement afficher des instructions à la suite en fonction de certains mots clés entrés par l’utilisateur dans le faux terminal.

Code source javascript : http://co4fuiol57xfwjobszioknloyqejrxr7emsey5obnhsnwg23725jn6yd.onion/4ec0ce6db63dd91893187c4c2348dc2c1008d6443014da4dab569e3e4d724ceb/terminal.js

On peut voir dans le code source, écrit en dur le code de sortie qui était attendu.

Maintenant voici la façon de faire qui était réellement attendue.

Au départ on ne connait pas la clé. On on tente de rentrer n’importe quoi :

On se souvient dans le drive proton identifié lors du challenge "6h00" il y avait un texte en russe qu’on a traduit en français et qui donnait (on reprend ici que la partie qui nous intéresse) :

```
...

Si tu as oublié la clé :
Dans le nom de celui qui a construit le mausolée du leader, réside le pouvoir d'arrêter la tempête.

...
```

Dans ce texte on y fait référence au pseudo du leader de l’organisation APT qu’on recherche lors de l’enquête qui est : L3n1n3

Donc en français : Lénine

Si on regarde où est enterré Lénine, on y retrouve bien le Mausolée qui est cité dans le texte traduit :

Le constructeur de ce Mausolée est Alexeï Chtchoussev :

Donc la clé est le nom de cette personne :

Nous avons réussi à arrêter le crash du satellite et retrouvé le code de retour.

Flag:`0x95BF4A`

---

# Checkmate

## Échec et mat

Et voilà ! C’est la fin de ce CTF (ou presque pour ceux qui n’ont pas fait les challenges bonus).

L’histoire se termine ici et nous réussissons à arrêter le crash du satellite juste à temps 💪

Je vous invite quand même à aller regarder les solutions des challenges bonus qui se situent en dessous 👀

Flag:`finish`

---

# Bonus

## Une politique non respectée

Les challenges bonus sont des challenges qui ne sont pas obligatoires pour terminer l’histoire du CTF mais sont nécessaires afin d’obtenir tous les points.

Voir le challenge "Command And Control" dans lequel on avait eu accès à une sorte de terminal émulé sur lequel on pouvait exécuter certaines commandes dont une pour extraire des utilisateurs ainsi que leur mot de passe hashé correspondant :

```
root : 240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9
stellalaunchsolutions : 008c70392e3abfbd0fa47bbc2ed96aa99bd49e159727fcba0f2e6abeb3a9d601
```

Les mots de passe sont hashés via SHA256 (soit par détection visuelle avec l’expérience, soit via des sites comme https://www.tunnelsup.com/hash-analyzer/).

On peut donc les "cracker" avec des outils en ligne comme Crackstation ou bien en offline avec hashcat ou JohnTheRipper par exemple.

On arrive à récupérer les mots de passe en clair pour l’utilisateur`root` et`stellalaunchsolutions`:

Mais seul celui de root nous intéresse ici.

Flag:`admin123`

---

## Altitude

La description de la photo correspond à celle prise par Arina et postée sur son profil Mastodon trouvé lors du challenge "La clé financière"

Une simple recherche inversée avec Google Lens nous donne directement le nom du lieu :

On vérifie manuellement en s’y rendant avec Google Street View et on retrouve les éléments de base de la photo originale. Notamment le bord du toit, les mêmes massifs montagneux au loin ainsi que la palteforme sur laquelle les gens sont situés (même si ici on ne la voit pas, on devine son emplacement) : https://www.google.com/maps/@46.5547801,8.0058745,3a,75y,67.27h,84.45t/data=!3m8!1e1!3m6!1sAF1QipNwru4uS5FCpFC6ST51_PJEGOcpZY0Z_YR7XEFj!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipNwru4uS5FCpFC6ST51_PJEGOcpZY0Z_YR7XEFj%3Dw203-h100-k-no-pi-0-ya229.46938-ro0-fo100!7i8704!8i4352?entry=ttu

La photo a l’air d’avoir été prise à partir de la terrasse du bâtiment juste derrière nous. On s’y positionne donc et on récupère les coordonées GPS :

Flag:`46.554, 8.005`

---

## Sur les traces de l’amende helvétique

Ce challenge fait suite à celui se nommant "Un bon bol d’air" et dans lequel on identifie le lieu comme étant "Harder Kulm" en Suisse.

Cette photo a été prise le 4 avril 2024 donc il s’agit de celle-ci.

Apparemment il y a un élément emblématique de la Suisse. On va donc simplement se rendre sur Maps pour vérifier : https://www.google.com/maps/@46.6972457,7.8516718,3a,75y,186.83h,81.98t/data=!3m8!1e1!3m6!1sAF1QipPlWiw2_NKNvlqKCTLL2JTMyb_G7io7dd67IxbT!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipPlWiw2_NKNvlqKCTLL2JTMyb_G7io7dd67IxbT%3Dw203-h100-k-no-pi-0-ya50.332417-ro-0-fo100!7i9728!8i3976?entry=ttu

Si on regarde les éléments emblématiques de la Suisse sur Google :

Le chocolat se fait avec du lait. Le chocolat Suisse est très réputé donc ça correspond à l’élément que nous recherchons.

Il semble y avoir une sorte d’affiche sur la vache mais on ne réussi pas à la lire avec cet angle :

On rappelle qu’on doit trouver une amende liée à cet objet. Rechercher sur Internet par rapport à cet évènement ne nous donne rien. Nous avons essayé de chercher s’il y avait des journaux locaux qui en parlaient mais nous n’avons rien trouvé.

A certains moments ce n’est pas la même vache à l’emplacement habituel. Peut-être s’est-il passé quelque chose avec, qu’ils l’ont remplacé et donc indiqué une amende sur l’affiche posée sur la nouvelle vache ? Peut-être.

Si on se promène un peu en Street View on voit effectivement une ancienne sculpture de vache qui a l’air abîmée :

Après avoir passé un peu de temps à tourner en rond on trouve enfin un point qui nous permet de lire l’affiche. Effectivement on y trouve bien le montant de l’amende en cas d’infraction : https://www.google.com/maps/@46.6971812,7.8516831,3a,65.1y,25.81h,67.04t/data=!3m8!1e1!3m6!1sAF1QipO-GTp5kcTuFzI3KR2Lv_edNxKFfOLNPq4RK5cp!2e10!3e11!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipO-GTp5kcTuFzI3KR2Lv_edNxKFfOLNPq4RK5cp%3Dw203-h100-k-no-pi-0-ya171.58337-ro-0-fo100!7i7776!8i3888?entry=ttu

Flag:`50`