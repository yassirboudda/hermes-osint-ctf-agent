# Source: https://github.com/Tacosint/Write-up_Hunt_AEGE_2022

# File: writeup.md

# Write-up HUNT EGE 2022 - OSINT CTF
### By Eldwiin & Zmondy & R0ck3t & Yui (aka Kipixelle) & Tab - Equipe Tacosint

# Sommaire
- [Write-up OSINT](#Write-up-OSINT)
  - [Nouveau Dossier](#Nouveau-Dossier)
  - [Tic Tac](#Tic-Tac)
  - [Voyage Voyage](#Voyage-Voyage)
  - [7e ciel](#7e-ciel)
  - [L'anarchiste](#Lanarchiste)
  - [La boîte de Pandore](#La-boîte-de-Pandore)
  - [Escapade nocturne](#Escapade-nocturne)
  - [Cupidon](#Cupidon)
  - [Cryptex](#Cryptex)
  - [Le conciliabule](#Le-conciliabule)
  - [Tornado](#Tornado)
- [Write-up Escape game](#Write-up-Escape-game)
  - [Place du Canada](#Place-du-Canada)
  - [City Locker](#City-Locker)
  - [Désamorçage](#Désamorçage)
- [Rapport](#Rapport)
- [Maltego](#Maltego)

# Write-up OSINT
Ce write-up va se concentrer uniquement sur la partie d’investigation que nous avons eu à effectuer en première partie de journée.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image14.png)

## Nouveau Dossier

> Vous êtes un enquêteur faisant partie d’une entreprise très discrète qui gère des situations de crise, souvent liées à des activités illégales, pour des clients fortunés. Cependant, les moyens d’action à votre disposition demeurent uniquement légaux. Vous gérez ces situations sensibles avec discrétion et tact, ce qui participe à la confiance accordée par vos clients.
> 
> Vous et votre équipe venez d’être mandaté pour aider une personne visiblement en grande difficulté. Les éléments dont vous disposez sont flous. En effet, vous n’avez accès qu’à une vidéo envoyée par le client comme point de départ de cette enquête qui est extrêmement pressante.
> 
> Pour chaque flag, le format vous sera spécifié. En cas de doute, contacter un admin sur Discord
>
> Format du flag : hunt{flag}


Premier challenge pour poser le cadre, ici, rien de compliqué, seulement recopier le flag :  **hunt{flag}** .

## Tic Tac
> Les propos du jeune homme étaient confus mais il compte sur nous pour régler cette affaire discrètement. A quelle heure la bombe explosera-t-elle ?
> https://www.youtube.com/watch?v=5CAEPpIKYNc


Afin de déduire l’heure de l’explosion de la bombe, il fallait récupérer le décompte affiché sur celle-ci lors de la vidéo. A partir de ce décompte, il fallait ensuite se référer au moment de la vidéo où le décompte apparaissait. On avait donc, grâce à cela le temps entre le début de la vidéo, et l’explosion de la bombe. Heureusement pour nous, le nom de la vidéo n’a pas été changé avant d’être téléversée sur Youtube ! Ce nom comprend donc l’instant auquel la vidéo a été prise (date et heure du début de la vidéo -> 202205210725 YYYYMMDDHHmm). 

Pour finir, il fallait additionner tout cela :  
- HeureVideo + (Decompte + TempsVideo) = HeureExplosion
- 07h25 + (1m14 + 10h07m09)= 17h33m23

Pour la réponse du challenge, les secondes ne nous intéressaient pas, ce qui nous donne  **hunt{17:33}** .

## Voyage Voyage
> Où notre protagoniste a-t-elle étudié ?

Cette question porte sur une certaine “protagoniste”. Celle-ci n’est autre que Emilie Rochefort, assistante parlementaire, dont la carte de visite apparaît dans la vidéo du challenge précédent.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image3.png)

Avec son nom, son prénom et son occupation, une recherche sur linkedIn nous permet de retrouver son [profil Linkedin](https://fr.linkedin.com/in/emilierochefort1850) : 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image25.png)

Ce profil linkedIn, et plus particulièrement son CV posté dessus nous permet de découvrir une adresse e-mail : `emilierochefort1850@gmail.com` ainsi que le lieu où elle a étudié. Le lieu qui nous intéresse ici, est celui situé à l’étranger, Bucarest, qui est la capitale de la Roumanie. 

Le flag est donc le suivant : **hunt{bucarest_roumanie}** .

## 7e ciel
> Emilie Rochefort est une personne d'intérêt.
> 
> Un compte crucial pour la suite de l'enquête se cache dans les publications d'une de ses connaissances.
>
> Quel est ce compte ?

Dans ce challenge, nous recherchons donc une nouvelle personne qui est proche d’Emilie. Les informations proposées avec le seul compte que nous avons en notre possession ne nous mène à rien. Nous sommes donc allés chercher de nouveau comptes d’Emilie sur les réseaux sociaux. Le mail que nous avons précédemment récupéré (emilierochefort1850@gmail.com) nous donne seulement des informations sur le fait que celle-ci est utilisée sur le site nike.com, strava.com et flickr.com. Il nous faut donc chercher ailleurs. Nous partons donc pour rechercher “Emilie Rochefort” sur Facebook. Plusieurs comptes nous sont remontés. 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image18.png)

Le premier (https://www.facebook.com/emilierochefort1850) correspond bien à la personne que nous recherchons. Nous pouvons le vérifier en comparant les informations d’études récupérées sur LinkedIn et ce qui est proposé sur le profil Facebook. De plus, l’URL du profil concorde bien avec l’adresse mail que nous avions précédemment (emilierochefort1850).

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image5.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image9.png)

Dans la section “A propos” de ce nouveau compte Facebook, nous pouvons voir qu’Emilie est en couple avec un certain [Hervé de Montaclerc](https://www.facebook.com/profile.php?id=100080713629687). 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image33.png)

Très bonne piste, cependant, ce n’est pas la réponse au challenge. Le format du flag à trouver est sous la forme hunt{@compte}. Ce format nous fait tout de suite penser à Twitter. Cherchons donc si ce Hervé à un compte Twitter. En parcourant les publications sur Facebook, pas d’éléments à ce sujet. Voyons si notre intuition est bonne, et allons directement sur Twitter pour trouver s’il a un compte. Une simple recherche sur Twitter nous renvoie le compte d’un certain [“Angevin amoureux” @montaclerc](https://twitter.com/montaclerc). 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image41.png)

L'orthographe correspond et sur son facebook on peut voir qu’il vient de la ville d’Angers. C’est bien ce compte que nous cherchons. 

Le flag est donc :  **hunt{@montaclerc}**.

## L'anarchiste 
> L'intuition était bonne, ce nouveau protagoniste cache quelque chose. Une de ses amies semble véhiculer des messages politiques. Qui est la figure dont elle déclare s'inspirer ?

Grâce au [compte Facebook d’Hervé](https://www.facebook.com/profile.php?id=100080713629687), nous avons pu voir les différentes relations qu’il entretient. Il semble plutôt proche (même si la relation est parfois houleuse) d’une certaine Alice.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image40.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image16.png)

Cependant, cela ne semble rien donner du côté de cette Alice. Cette Ludivine qui apparaît sur le dernier screen semble aussi intéressante. Bingo ! Sur son facebook, [Ludivine](https://www.facebook.com/profile.php?id=100080516294168) partage beaucoup de contenus à caractère anarchiste. De plus, en changeant sa photo de couverture, celle-ci déclare que l’homme qui est dessus est son “inspiration”. 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image15.png)

Or, une recherche inversée sur google image nous permet très vite de découvrir que cet homme n’est autre qu’Auguste Vaillant, un anarchiste français qui avait jeté une bombe dans la chambre des députés. 

Le flag est donc le suivant : **hunt{Auguste_Vaillant}** .

## La boîte de Pandore
> Nos investigations confirment qu'Emilie semble avoir une présence en ligne conséquente. Une enseigne revient à plusieurs reprises dans ses publications, pouvez-vous nous dire laquelle ?

A l’aide de l’adresse mail récupérée sur le CV d’Emilie, nous avons utilisé l’outil [holehe](https://github.com/megadose/holehe) qui nous a permis de voir qu’Emilie possède un compte [Strava](https://www.strava.com/athletes/103168254) et un compte [Flickr](https://flickr.com/photos/195642122@N06) associés à cette adresse mail. Or, sur le compte Flickr, nous pouvons voir qu’Emilie s’est prise en photo devant un City Locker. 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image32.png)

De plus, en analysant les courses réalisées sur Strava, nous pouvons remarquer qu’elles finissent (presque) toutes devant un city locker.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image47.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image44.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image34.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image13.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image49.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image6.png)

Le flag est donc le suivant :  **hunt{city_locker}** .

## Escapade nocturne 
> Emilie semble s'être intéressée à cette enseigne à plusieurs reprises. Reste à déterminer pourquoi ?
> 
> Des informations pouvant vous aider à accéder à ces lieux sont certainement dissimulées quelque part. Retrouvez-les !

Comme découvert lors du challenge précédent, Emilie possède un compte Strava. C’est sur celui-ci que se trouvent les informations qui nous intéressent pour ce challenge. En effet, sur son compte Strava, les trajets menant à un city locker sont accompagnés  d’un message du type : Uşă : #988795#.

Il se trouve que "Uşă” en roumain signifie “porte”. Cela rejoint ce que l’on avait identifié précédemment avec le city locker (enseigne permettant de stocker des affaires dans un casier protégé par un code). 

Il suffit donc de rassembler les différents codes utilisés pour pouvoir obtenir le flag suivant : **hunt{#881562##988795##468359#}**.

## Cupidon 
> Quand se sont mis en couple nos deux tourteraux ?

Bien, maintenant, il nous faut trouver la date de mise en couple d’Emilie et de Hervé. Dans le “A propos” de leur compte Facebook, nous pouvons voir qu’ils se sont mis en couple en 2021. Nous avons donc l’année. Maintenant il ne reste plus que le jour et le mois. Aucune mention de cette date dans leurs publications. 

En suivant le super guide s’intitulant [[Guide & astuces OSINT #1] Facebook Search ou comment percer les profils privés](https://portail-ie.fr/analysis/2991/guide-astuces-osint-1-facebook-search-ou-comment-percer-les-profils-prives) écrit par le Club OSINT & Veille AEGE en décembre 2021, nous pouvons trouver la réponse. En se rendant sur le profil Facebook d’Emilie, nous effectuons tout simplement une recherche de mots clés grâce à la fonctionnalité “Recherche” de Facebook. Cette fonctionnalité permet de rechercher l’activité de la personne dans des pages/groupes, sur les commentaires effectués sur d’autres profils, etc. 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image39.png)

Etant donné que nous recherchons une date de mise en couple (ou un anniversaire de relation), nous pouvons rechercher via des mots-clés en rapport avec cela. Nous optons pour le mot clé “aime”, et tombons ainsi sur plusieurs publications d’Emilie cherchant une destination pour fêter leur 1 an, le 29 mai. 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image48.png)

Super ! Nous avons donc maintenant leur date complète ! Nous pouvons valider le flag  **hunt{29/05/2021}** .

## Cryptex 
> Un autre ami de nos protagonistes, fan d'Amsterdam, aime communiquer sur Internet. Toutefois un de ses messages est incompréhensible. Aidez-nous à y voir plus clair.

A partir du Twitter d’Hervé, nous avons identifié 3 followers : 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image21.png)

Même si “Basile ou Baz” et son régime BFM semblent intéressant, le fait que Erwan Lagadec soit un “FR guy in Amsterdam” colle plutôt bien avec nos recherches. Son compte [twitter](https://twitter.com/ErwanLagadec1) nous donne directement le lien vers son compte [Tumblr](https://www.tumblr.com/blog/view/erwan97-29). Sur son compte, une image en noir et blanc de ce qui semble être une manifestation nous indique que nous sommes sur la bonne piste ! De plus, un “message incompréhensible” a été posté par celui-ci : “ZmxhZ3tjcnlwdGV4OjUvMTMvNS8yMS8yMC81fQ==”. Les investigateurs avertis auront reconnu de la base 64. Un petit tour sur [Cyberchef](https://gchq.github.io/CyberChef/) nous permet de décoder ce message :  flag{cryptex:5/13/5/21/20/5} .

Une petite transformation au bon format nous donne le flag suivant :  **hunt{cryptex:5/13/5/21/20/5}** .

## Le conciliabule 

> Recoupez tous les éléments que vous avez trouvés jusque là. Ces derniers nous mènent vers le même personnage historique. La fascination de nos protagonistes pour cette figure est intrigante. Il semblerait qu'ils ont même traduit une page exprès en son nom.
>
> Visiblement, le diable se cache dans les détails.

Nous sommes arrivés de différentes manières à la page traduite. La première manière repose sur la vidéo du premier challenge. En effet, dans cette vidéo, sur la main du protagoniste est inscrit “Emile Révolte”. Cela nous a donc donné un pseudo à rechercher. Or, dans les tweets et réponses sur [Twitter d’Hervé de Montaclerc](https://twitter.com/montaclerc/with_replies), il se trouve qu’il a eu une altercation avec un certain [@emilereevolte](https://twitter.com/Emilereevolte).

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image36.png)

Outre l’information concernant la taille d’Hervé, cela nous permet surtout de remonter à Jérome Baruel, et à son compte [copains d’avant](https://copainsdavant.linternaute.com/p/jerome-baruel-21033499) qu’il a partagé sur son twitter. Or, sur son compte copains d’avant, Jérome évoque 2 informations intéressantes pour l’enquête. Tout d’abord, il indique qu’il est contributeur wikipédia, et deuxièmement, il précise qu’il parle couramment roumain.

Une recherche avec le pseudo émilerevolte et wikipédia nous permet de retrouver sa [page d’auteur](https://ro.wikipedia.org/wiki/Utilizator:Emile_revolt%C3%A9) sur le wikipédia roumain.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image24.png)

A partir de cet utilisateur, il est possible de récupérer toutes les modifications qu’il a effectuées (en roumain, c’est quand même beaucoup plus sympa). Pour cela, il faut aller dans [l’historique](https://ro.wikipedia.org/w/index.php?title=Utilizator:Emile_revolt%C3%A9&action=history) (istoric) puis cliquer sur les [contributions](https://ro.wikipedia.org/wiki/Special:Contribu%C8%9Bii/Emile_revolt%C3%A9) de cet auteur (contribuții). Ici, on découvre qu’Emile a créé la page roumaine d’un certain Auguste Vaillant. Tiens, ce personnage ne nous est pas inconnu ! La seconde façon d’arriver à cette page consistait à chercher directement Auguste Vaillant qui est revenu plusieurs fois dans les comptes étudiés, sans passer par la partie historique des contributions d’Emile.

Une fois sur cette page, il faut utiliser la fonction d’historique pour afficher la [version créée par Emile](https://ro.wikipedia.org/w/index.php?title=Auguste_Vaillant&oldid=14919495). En effet, un passionné roumain (que l’on salue au passage) a modifié la page seulement 2h après la création de celle-ci. Sur la page créée par Emile, à l’aide d’un traducteur, on remarque que la légende de l’image est très spéciale. Celle-ci peut se traduire par : “Ce qu'il y a à l'intérieur compte”. L’image nous paraît donc tout de suite très attirante. Grâce à un super outil nommé [Aperi’solve](https://aperisolve.fr/) (attention de bien télécharger la photo originale), nous découvrons caché dans l’image le texte suivant : "{t.me/anarchistedetaregion}". Ce message, en plus d’être le flag, nous donne accès à un channel telegram. 

Le flag est donc : **hunt{t.me/anarchistedetaregion}** .

## Tornado 
> Vous avez réussi à accéder au canal de communication de nos protagonistes. Mais à la lecture de leurs communications, on comprend rapidement qu'ils communiquent par code. A tel point que l'on a du mal à savoir où tout ça nous mène …
> 
> Avez-vous une idée ?


Sur le channel Telegram, nous trouvons une conversation fort intéressante pour la suite de l’enquête. Outre les informations croustillantes en elles-mêmes, nous disposons aussi d’une archive qui indique apparemment le lieu de rendez-vous. Cette archive est un zip contenant 10 dossiers numérotés de 0 à 9, et ce de manière récursive. Au “fond” de chaque chemin se trouve une image nommée “0.png”, sauf une image qui sort du lot. Pour l’identifier, nous avons utilisé 2 méthodes. 
- La première, avec un “tree” sous linux qui permet d’afficher l’arborescence. Le nom de l’image concernée saute aux yeux. 
- La seconde, se base sur le fait que tous les dossiers font environ la même taille, sauf celui qui contient cette image qui est bien plus lourde que les autres (cela se remarque facilement avec un décompresseur d’archives comme winrar par exemple).

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image7.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image17.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image11.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image50.png)

Cette image intitulée “hranest calul.png” se situe dans le dossier 0/3/6. Cependant cette image n’est pas exploitable en l'état.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image20.png)

Comme pour le challenge précédent, utilisons [Aperi’solve](https://aperisolve.fr/) afin de découvrir ce qui se cache derrière cette image ! Via les filtres bleus, l’outil nous montre l’image suivante : 

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image10.png)

Ils doivent donc se retrouver place du canada à Paris ! Ça tombe bien, ce n’est pas si loin de l’EGE… Le flag est le suivant :  **hunt{place_du_canada}** .

# Write-up Escape game
## Place du Canada
Une fois arrivés place du Canada, nous reprenons les éléments afin de remonter la piste. L’image de l’épreuve précédente s’appelle “hranest calul”. Il s’agit d’une phrase en Roumain qui veut dire “Nourrir le cheval”. Ça tombe bien, il y a justement une statue de cheval sur la place. Nous trouvons donc un QRCode face à son museau, collé sur la plaque qui nous mène à une note sur pastebin (https://pastebin.com/1ApsfR7X).

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image37.png)

## City Locker
Suite à la découverte de la note pastebin, les organisateurs nous indiquent de nous diriger vers le casier n°11 pour la suite de l’enquête. Nous partons donc au City-Locker de Châtelet Les Halles situé 82 rue des Gravilliers, au pas de course bien évidemment.
Une fois sur place, nous ouvrons le casier et … surprise ! Il est vide !

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image30.png)

Après cette petite frayeur, il s’est avéré qu’une autre équipe était en train de résoudre le cryptex à l’extérieur, tout est rentré dans l’ordre. 

Nous récupérons le cryptex et le téléphone présents dans le casier et entrons donc les lettres correspondant à chacun des chiffres trouvés pour l’épreuve Cryptex : 5/13/5/21/20/5 qui donnent donc : EMEUTE. Le Cryptex s’ouvre et nous découvrons une carte sim, dissimulée dans un papier.

En l'insérant dans le téléphone, nous trouvons un code dans les brouillons des SMS : V843+xv.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image45.png)

Nous reconnaissons tout de suite un “Plus Code”. En l’entrant dans Google maps, il nous indique le 196 rue de Grenelle. Bingo ! Retour à l’EGE !

Les organisateurs nous demandent alors de retrouver le manuel complet en pdf et en français dont est issu le papier entourant la carte sim. Il s’agissait donc du manuel de jeu de “Keep Talking and Nobody Explodes”. 

## Désamorçage 
Nous retournons donc à l’EGE où les organisateurs nous attendent pour le challenge final : désamorcer la bombe. Après avoir relu la notice et en mettant à profit nos heures de jeu, nous désamorçons une bombe difficile avec 28 secondes restantes au compteur. Hervé et l’EGE sont sauvés ! Qui aurait cru que nos après-midi passées sur ce jeu auraient servi un jour ?

# Rapport
https://github.com/Tacosint/Hunt_AEGE_2021/blob/main/rapport.md

# Maltego
Pendant tout ce CTF, nous avons complété un Maltego avec les différentes informations que nous avons récoltées.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/maltego.png)



---

# File: rapport.md

# Rapport HUNT EGE 2022 - OSINT CTF
### By Eldwiin & Zmondy & R0ck3t & Yui (aka Kipixelle) & Tab - Équipe Tacosint🌮

## Contexte de la mission
Le commanditaire de la mission est Hervé de Montaclerc. Après s’être réveillé enfermé dans une salle bâchée avec une bombe près de lui, ce dernier nous a contacté afin de le retrouver et de désamorcer la bombe.

## Protagonistes
Les différents protagonistes sont :
- **Hervé De Montaclerc aka “L'angevin amoureux”**, commanditaire de la mission et ancien membre du groupe d’anarchistes décrit plus tard. Il l’a quitté après avoir appris la nature violente de leurs intentions.
- **Emilie Rochefort**, collaboratrice parlementaire et concubine de Hervé De Montaclerc depuis le 29 mai 2021.
- **Jérôme Baruel aka “Emile Révolte”**, chef du groupe terroriste ayant perpétré l’enlèvement et la pose de la bombe.
- **Erwan Lagadec**, membre du groupe terroriste ayant participé à l’enlèvement de Hervé.
- **Ludivine Moreaux**, membre active du groupe terroriste ayant participé à l’enlèvement de Hervé.
- **Alice Dllrd**,  membre du groupe terroriste.

## Déroulé des faits
- **Entre décembre 2015 et juillet 2016**, le groupe se forme pendant le semestre d’études en Roumanie d’Emilie à l’exception d’Hervé.   
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image23.png)  
*(noroc correspond correspond à la chance en Roumain)*

- Le **29 mai 2021**, Emilie et Hervé se mettent en couple. Hervé rejoint alors le groupe dans le but de manifester son opposition au gouvernement.  
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image43.png)

- Le **3 mai 2022**, Erwan crée un groupe Télégram afin d’organiser l’attaque que rejoindront Emile, Ludivine, Hervé. Alice y est également invitée mais n’a pas rejoint. Le groupe s’inspire d’Auguste Vaillant, anarchiste et terroriste français de la fin du XIXè siècle ayant fait exploser une bombe dans la chambre des députés. Après avoir traduit en roumain sa page Wikipédia, Erwan y a caché le lien du groupe Télégram dans la photo.

- Le **17 mai 2022**, Emilie obtient un badge d’assistante parlementaire qu’Hervé partage au groupe. Ce badge leur permet de récupérer des documents.   
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image22.png)  
Au vu des déplacements d’Alice trouvés sur Strava, il semblerait qu’elle ait récupéré ces mêmes documents le soir même. Le même jour, elle loue des casiers dans Paris. Dans un de ces casiers est découvert un téléphone contenant l’emplacement de la bombe.  
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image29.png)  

- Le **20 mai 2022**, Hervé découvre que l’objectif du groupe n’est pas de faire de la désobéissance civile pacifiste et de l’extraction de document mais de préparer une action violente par le biais d’une bombe placée à l’EGE, au 196 rue de Grenelle et détonnant à 17h33. Il décide alors de se désolidariser du groupe. Il en fait part au groupe sur Télégram et publie un tweet, supprimé peu de temps après.  
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image38.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image26.png)

- Emile demande alors à Ludivine et Erwan de surveiller Hervé puis de l’enlever. C’est en se réveillant dans la salle après cet enlèvement qu’il nous a contactés par téléphone et transmis la vidéo.  
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image52.png)

## Suppositions
Nous ne sommes pas certains de l’implication d’Emilie. Elle n’est pas présente sur la conversation Telegram et nous ne savons pas si c’est elle qui a placé le téléphone relié à la bombe dans son casier. Néanmoins, nous supposons qu’elle ait connaissance des faits et qu’elle ait participé à l’extraction des documents en utilisant son badge. Son compte Strada serait le relais pour indiquer l’emplacement des casiers où se trouvent les documents ainsi que d’en transmettre les codes et le moment auquel les documents y sont déposés.  

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image51.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image35.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image31.png)
![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image42.png)


---

# File: README.md

# Write-up HUNT EGE 2022 - OSINT CTF
### By Eldwiin & Zmondy & R0ck3t & Yui (aka Kipixelle) & Tab - Equipe Tacosint

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image28.jpg)

# HUNT EGE 2022
## CTF
Le CTF Hunt by EGE est un CTF OSINT couplé à une traque sous la forme d'un « escape game » dans Paris intra-muros. La 2ème édition s’est déroulée le samedi 21 mai 2022 dans les locaux de l’EGE. Celui-ci est entièrement organisé par le [Club OSINT & Veille de l'AEGE](https://www.aege.fr/groupe/club-osint-veille-18). Cette édition fut composée d’une première partie de challenges où il fallait retrouver des informations appelées “flags”, ainsi qu’une deuxième partie où il fallait se déplacer physiquement à des points donnés et résoudre des énigmes en lien avec la première partie de l’investigation. 

## Team
Nous avons participé à ce CTF sous le nom d’équipe Tacosint, qui était composée de 5 personnes (Eldwiin, Kipixelle, R0ck3t, Tab et Zmondy). Notre équipe a fini 2ème au classement général sur 13 équipes présentes.

![](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/images/image12.png)


# Write-ups
## Markdown
  - [Write-up](https://github.com/Tacosint/Hunt_AEGE_2021/blob/main/writeup.md)
  - [Rapport](https://github.com/Tacosint/Hunt_AEGE_2021/blob/main/rapport.md)
## PDF
  - [Write-up + Rapport](https://raw.githubusercontent.com/Tacosint/Hunt_AEGE_2021/main/Write-up_HUNT_EGE_2022_Tacosint.pdf)

