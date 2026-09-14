# Source: https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026

# File: Writeup.md

# Write-up TACOSINT - L'appel de la forêt 2026 - OSINT CTF

### By Eldwiin & Kipixelle & R0ck3t & Tab & Zmondy - Team Tacosint

# Sommaire

- [L’appel de la forêt](#lappel-de-la-forêt)
    - [CTF](#ctf)
    - [Remerciements](#remerciements)
- [Write-up](#write-up)
    - [Dépendance des challenges et informations](#dépendance-des-challenges-et-informations)
    - [Intro](#intro)
        - [Welcome](#welcome)
        - [Reportage animalier](#reportage-animalier)
    - [Chapitre 1 \- Introduction](#chapitre-1---introduction)
        - [Chill comme un capybara](#chill-comme-un-capybara)
        - [Sous l’oeil du Sphynx](#sous-loeil-du-sphynx)
        - [\[BONUS\] Le sens de l'orientation d'un chat](#bonus-le-sens-de-lorientation-dun-chat)
    - [Chapitre 1 \- La Famille Michelle \[BONUS\]](#chapitre-1---la-famille-michelle-bonus)
        - [\[BONUS\] La coquetterie du paon](#bonus-la-coquetterie-du-paon)
        - [\[BONUS\] La générosité d'une Girafe](#bonus-la-générosité-dune-girafe)
        - [\[BONUS\] Le grand rêve d'un Tatou](#bonus-le-grand-rêve-dun-tatou)
        - [\[BONUS\] Cachée comme un phasme](#bonus-cachée-comme-un-phasme)
        - [\[BONUS\] Le câlin du chimpanzé](#bonus-le-câlin-du-chimpanzé)
        - [\[BONUS\] La balade du zèbre](#bonus-la-balade-du-zèbre)
    - [Chapitre 1 \- Fait divers \[BONUS\]](#chapitre-1---fait-divers-bonus)
        - [\[BONUS\] L'envol des perroquets](#bonus-lenvol-des-perroquets)
        - [\[BONUS\] Le trésor des corbeaux](#bonus-le-trésor-des-corbeaux)
        - [\[BONUS\] L'insouciance du paresseux](#bonus-linsouciance-du-paresseux)
    - [Chapitre 1 \- Petsitter](#chapitre-1---petsitter)
        - [La mésange babysitter](#la-mésange-babysitter)
        - [Bavard comme une pie](#bavard-comme-une-pie)
        - [Pris dans la toile](#pris-dans-la-toile)
        - [Le terrier du lapin](#le-terrier-du-lapin)
    - [Chapitre 2 \- Acte 1](#chapitre-2---acte-1)
        - [Tapir dans l'ombre](#tapir-dans-lombre)
        - [Le Caméléon des internet](#le-caméléon-des-internet)
        - [Les piqueboeufs et l'hippopotame](#les-piqueboeufs-et-lhippopotame)
    - [Chapitre 2 \- Acte 2 \- Activités](#chapitre-2---acte-2---activités)
        - [La parade du paon](#la-parade-du-paon)
        - [Les Traces de l'Ours](#les-traces-de-lours)
        - [La chasse du guépard](#la-chasse-du-guépard)
        - [Les Abysses des Lophiiformes](#les-abysses-des-lophiiformes)
    - [Chapitre 2 \- Acte 2 \- Droit](#chapitre-2---acte-2---droit)
        - [\[BONUS\] Les fourberies du renard](#bonus-les-fourberies-du-renard)
        - [Le loup déguisé](#le-loup-déguisé)
        - [Les commencements de l'oiseau](#les-commencements-de-loiseau)
        - [Le Territoire du Loup](#le-territoire-du-loup)
    - [Chapitre 2 \- Acte 2 \- Développement](#chapitre-2---acte-2---développement)
        - [La Mémoire de l'Éléphant](#la-mémoire-de-léléphant)
        - [Le Nid Douillet](#le-nid-douillet)
        - [\[BONUS\] La Fourmilière d'Informations](#bonus-la-fourmilière-dinformations)
    - [Chapitre 2 \- Acte 3 \- Communication](#chapitre-2---acte-3---communication)
        - [La danse des abeilles](#la-danse-des-abeilles)
        - [L'Instinct du Pigeon Voyageur](#linstinct-du-pigeon-voyageur)
        - [\[BONUS\] Le Mille Pattes](#bonus-le-mille-pattes)
    - [Chapitre 2 \- Acte 3 \- Financement](#chapitre-2---acte-3---financement)
        - [L'Épine de l'Oursin](#lépine-de-loursin)
        - [La Pieuvre et ses Tentacules](#la-pieuvre-et-ses-tentacules)
        - [\[BONUS\] L'astuce du Singe](#bonus-lastuce-du-singe)
    - [Chapitre 2 \- Acte 3 \- Organisation](#chapitre-2---acte-3---organisation)
        - [La Toile du Tisserin](#la-toile-du-tisserin)
        - [La traque du faucon](#la-traque-du-faucon)
        - [La colère du dragon](#la-colère-du-dragon)
        - [Le radar de la chauve-souris](#le-radar-de-la-chauve-souris)
        - [L'énergie du frelon oriental](#lénergie-du-frelon-oriental)
        - [\[BONUS\] La Ruche et la Reine](#bonus-la-ruche-et-la-reine)
    - [Chapitre 2 \- Acte 3 \- Transport](#chapitre-2---acte-3---transport)
        - [Dans le sillage du cachalot](#dans-le-sillage-du-cachalot)
        - [La caravane de dromadaires](#la-caravane-de-dromadaires)
        - [La Migration de la Cigogne](#la-migration-de-la-cigogne)
        - [La nuée de chauves-souris](#la-nuée-de-chauves-souris)
        - [La tanière du lion](#la-tanière-du-lion)
    - [Chapitre 2 \- Acte 4](#chapitre-2---acte-4)
        - [Le Piège de l'Araignée](#le-piège-de-laraignée)
        - [La hiérarchie de la meute](#la-hiérarchie-de-la-meute)
        - [Noctua](#noctua)
        - [Tusko](#tusko)
        - [Panthera](#panthera)
        - [Scorpiox](#scorpiox)
        - [La nuit de la panthère](#la-nuit-de-la-panthère)
    - [Chapitre 2 \- Fin](#chapitre-2---fin)
        - [La joie du quokka](#la-joie-du-quokka)
    - [Chapitre 3](#chapitre-3)
        - [Le Silence des Mouettes](#le-silence-des-mouettes)
    - [Chapitre 3 \- Crime](#chapitre-3---crime)
        - [Le festin du vautour](#le-festin-du-vautour)
        - [La Vigile du Hibou](#la-vigile-du-hibou)
        - [Le venin du Taïpan](#le-venin-du-taïpan)
        - [Le caillou de la loutre](#le-caillou-de-la-loutre)
    - [Chapitre 3 \- Péhuson](#chapitre-3---péhuson)
        - [Chargé comme une mule](#chargé-comme-une-mule)
        - [La protection de la tortue](#la-protection-de-la-tortue)
        - [La taupe](#la-taupe)
        - [Hors de la Tanière](#hors-de-la-tanière)
    - [Chapitre 4](#chapitre-4)
        - [La vraie joie du quokka](#la-vraie-joie-du-quokka)
- [Résumé de l’histoire](#résumé-de-lhistoire)

#

# L’appel de la forêt

## CTF

L’*appel de la forêt* est un CTF 100% OSINT, se déroulant en ligne, avec une partie compétitive du 03 juillet 20h00 CET (UTC+1) au 09 juillet 2026 20h00 CET (UTC+1). Créé par l’association *Tacosint*, il a comme partenaires **Badgeforge**, 
**OscarZulu** et **EPIEOS**.  
*Tacosint* est composée des membres suivants :

- **Eldwiin**
- **Kipixelle**
- **R0ck3t**
- **Tab**
- **Zmondy**

## Remerciements

Nous souhaiterions remercier toutes les personnes qui nous ont accompagnés lors de la création de ce CTF !

- [**BadgeForge**](https://www.badgeforge.eu/), [**Oscar Zulu**](https://oscarzulu.org/), [**EPIEOS**](https://epieos.com/), nos sponsors et fournisseurs des lots ;
- [**ElueTime**](https://eluetime.carrd.co/), notre super graphiste, pour la création du logo, des emotes, ainsi que des
  badges ;
- [**Oscar Zulu**](https://oscarzulu.org/) et [**Boosty**](https://www.linkedin.com/in/stevendfs/) pour leurs conseils
  sur la création du CTF ;
- [**Oscar Zulu**](https://oscarzulu.org/) et [**Hack'olyte**](https://hackolyte.fr/) pour les plugins sur le CTFd ;
- Nos **betatesteurs** et personnes qui nous ont supportés tout au long de la création du CTF ;
- **Les joueurs** pour leur persévérance et leur bonne humeur durant ce CTF.

# Write-up

## Dépendance des challenges et informations

L’ordre de déblocage des challenges est le suivant.  
![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image23.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image95.png)
![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image197.png)
![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image56.png)
![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image123.png)
![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image189.png)
![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image108.png)

Pour accompagner le write-up, vous trouverez un zip importable dans [Zero-Neurone](https://zeroneurone.com/) qui
contient les principaux éléments trouvés lors de l’enquête et notamment les liens entre les personnages. Il contient
plusieurs onglets dont un pour la partie crypto, et un pour la partie transport (visualisable sur la carte).
Pour la majorité des challenges, plusieurs formats de réponse étaient acceptés.

## Intro

### Welcome

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image154.png)

Le premier challenge a pour objectif de demander aux joueurs de lire le règlement pour obtenir le flag : `J'ai lu le règlement, et je m'engage à le respecter`

### Reportage animalier

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image70.png)

Ce second challenge a pour objectif de présenter le thème du CTF.  
Une **recherche sur *Google*** avec les termes `vol animaux compagnies race 2024 france télévision octobre` permet de
retrouver dans les premiers résultats [un article de **france télévision**](https://www.franceinfo.fr/environnement/biodiversite/animaux/animaux-les-vols-de-chiens-de-race-un-phenomene-en-pleine-expansion_6859943.html).  
Cet article indique “2 400 vols signalés en ligne depuis le début de l'année”. Le flag est donc : `2400`

## Chapitre 1 \- Introduction

### Chill comme un capybara

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image44.png)

Dans l'énoncé, plusieurs **indications** attirent notre attention :  
\- On cherche un **réseau social**  
\- Renée habite proche d'un ***"supermarché du coin Route d'Olivet"***

Pour le **supermarché**, une **recherche sur google maps** permet de faire ressortir deux possibilités : un **Auchan**
et un **Carrefour Market**, tous les deux à **Orléans**.

Pour le **réseau social**, on peut supposer qu’elle utilise ***Facebook*** qui semble être l'un des réseaux les plus
logiques à utiliser pour une personne âgée. Avec le prénom et nom **"Renée Michelle"** ainsi que l'indication **"
Orléans"**, on retrouve [le Facebook de Renée Michelle](https://www.facebook.com/profile.php?id=61578487714446).

Or, sur son compte, elle
a [posté une photo de son mari](https://www.facebook.com/permalink.php?story_fbid=pfbid02Xzr4K2LsaoAkZs5pJ1wB4tk8DvuJPdGVCcXm34BtHLWWWi4n3VwkW88fJWk2yXtel&id=61578487714446)
indiquant que le 24/03/2026 cela faisait **13 ans** que son mari était décédé. Le flag est donc : `24/03/2013`

### Sous l’oeil du Sphynx

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image162.png)

En regardant le ***Facebook*** de **Renée Michelle**, on peut identifier parmi ses **amis** des membres de sa famille,
dont [Sarah Michelle](https://www.facebook.com/michelle.sarah2003) qui a fait
un [post pour proposer à sa grand-mère le contact d’un petsitter](https://www.facebook.com/michelle.sarah2003/posts/pfbid02eroqFYbcZegS1mLgMMj7Mez7bLNgzFKSNECCAgfwuk92hKMy6CwLrHzVQuQT5i3Pl).
Renée Michelle indique le contacter dans la journée, ce qui montre que cette dernière est très intéressée par le **petsitter**. Sur la **photo** du post se trouve le **numéro du petsitter**. Le flag est donc : `0261913352`

### \[BONUS\] Le sens de l'orientation d'un chat

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image168.png)

Malo a disparu à **Orléans** proche de la route d’Olivet et on cherche la **SPA autonome régionale** la plus proche. Une
recherche sur la SPA d'Orléans nous permet de trouver le [site de la SPA du centre](https://www.spa-du-centre.com/). Sur
ce site, plusieurs **refuges** sont indiqués, et tous acceptent les chats. Le refuge situé **20 Chemin du Pont Cotelle à
Orléans** est le plus proche du **supermarché route d’Olivet**. Son numéro est indiqué directement sur le site. Le flag
est donc : `0238448964`

## Chapitre 1 \- La Famille Michelle \[BONUS\]

### \[BONUS\] La coquetterie du paon

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image182.png)

**L’URL** du compte ***Facebook*** de **Sarah** est **personnalisée** : **michelle.sarah2003**. En cherchant sur
différents **réseaux sociaux** avec ce “pseudo” (ou bien avec [maigret](https://github.com/soxoj/maigret)
ou [RhinoUserChecker](https://github.com/degun-osint/RhinoUserChecker)), il est possible de
retrouver [son compte Instagram](https://www.instagram.com/michelle.sarah2003/). Or, en **biographie** de ce dernier,
elle indique sous quel **pseudo** elle est aussi connue. Le flag est donc : `UnderTheVeil03`

### \[BONUS\] La générosité d'une Girafe

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image45.png)

À partir du **pseudo** obtenu précédemment, **UnderTheVeil03**, une recherche via un outil
comme [osintisnotacrime.com](https://osintisnotacrime.com/app/search) ou [whatsmyname](https://whatsmyname.app/) permet
de retrouver la présence d’[un compte mastodon](https://gaygeek.social/@UnderTheVeil03) et
d’[un compte X](https://x.com/UnderTheVeil03). Sur son compte ***Mastodon***, **Sarah**
indique [dans un post](https://gaygeek.social/@UnderTheVeil03/116629547663802510) qu’elle va passer le **week-end du 3
juillet** pour faire du **bénévolat** au **Refuge de Limoges**. Le flag est donc : `Limoges`

### \[BONUS\] Le grand rêve d'un Tatou

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image178.png)

Sur son ***Instagram***, **Sarah** a partagé plusieurs **photos** de lieux en lien avec des **métiers** et indique
qu’elle y est allée à chaque fois avec sa **sœur**. Sur [son compte X](https://x.com/UnderTheVeil03), **Sarah** a
aussi [partagé un post](https://x.com/UnderTheVeil03/status/2062468267206127843) le **04/06/2026** indiquant que depuis
**2 mois, sa sœur la tanne avec son métier de rêve**. Or, 2 mois plus tôt, le **04/04/2026**, sur ***Instagram*** Sarah
a partagé [un post sur la cité de l’espace](https://www.instagram.com/p/DWtIGSzDN1_/) sur lequel on peut lire “devenez
astronaute !”. Le flag est donc : `Astronaute`

### \[BONUS\] Cachée comme un phasme

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image22.png)

Sur le [compte *Facebook*](https://www.facebook.com/profile.php?id=61577432904055) de **Lucia**, obtenu car elle est **amie** avec **Renée**,
dans [un de ses posts](https://www.facebook.com/permalink.php?story_fbid=pfbid02czh1i93qKPhqFgHCxVEx7FZ2FsheLWrvv8ctrNLnVhfLq6F6pQa9Nus2tQXZCKqDl&id=61577432904055),
elle indique qu’elle va passer le **week-end** au **même endroit** que celui de ses **40 ans**. Sa **date de naissance**
indiquée sur ***Facebook*** étant le **03/01/1982**, on sait qu’elle a eu **40 ans** le **03/01/2022**.
Or, [dans un post du 03/01/2022](https://www.facebook.com/permalink.php?story_fbid=pfbid0BZhZ28VtBrFj8Eh4dXEEKskBbU2HzCKtw171FouSPXPFZeJryngFCnpuLrHQffugl&id=61577432904055),
elle upload une **image** de la vue de sa chambre :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image76.png)

Une **recherche *Google*** image en se concentrant sur la **fresque** au premier plan permet de faire
ressortir [un site avec une image similaire](https://www.firenzemadeintuscany.com/en/article/palaces-historic-florence-architectural-masterpieces-not-to-miss/).  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image193.png)

Sur ce dernier, on peut trouver que le bâtiment pris en photo est le **Palazzo Guicciardini**. Sur ***Google Maps***,
une recherche des **hôtels à proximité** permet de faire ressortir une résidence située juste en face :

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image10.png)

Le flag est donc : `Residenza Benizzi`

### \[BONUS\] Le câlin du chimpanzé

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image151.png)

Sur le [compte *Facebook* de Jean Michelle Jr](https://www.facebook.com/profile.php?id=61579482161478), le fils de Renée
et mari de Lucia, il y
a [une photo de mariage](https://www.facebook.com/permalink.php?story_fbid=pfbid0D3yasUNwSQfJQUtnqBPTdad75xu5o1KpiKfhMSdEtKoSBb3kSgtVFVx6JQhRHYYql&id=61579482161478)
de Lucia et lui. Si l’on regarde le **“alt”** de **l’image** (fonction utilisée pour **décrire l’image aux malvoyants**,
comme indiqué
dans [un post de Sarah](https://www.facebook.com/michelle.sarah2003/posts/pfbid0wpMaFze4tYTgwr4NgzzXGdLJ9tFm2NzKhMK48dhzXbGDJzSoCvaQwvhbmFQxbhUxl)),
on peut voir le **message** suivant : “Le jour où Mlle Karlsson est devenue Mme Michelle” :

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image138.png)

Le flag est donc : `Karlsson`

### \[BONUS\] La balade du zèbre

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image71.png)

Sur son [compte *Facebook*](https://www.facebook.com/profile.php?id=61579482161478&sk=about), **Jean Michelle Jr**
indique dans ses centres d’intérêt qu’il fait de la **course à pied**. De plus, sa fille indique
dans [un post sur son compte *Mastodon*](https://gaygeek.social/@UnderTheVeil03/116504330659283172) qu’elle va courir
avec son père. Or, le réseau social le plus connu de course à pied est ***Strava***. Une recherche sur ***Strava*** avec
`Jean Michelle Jr` permet d’obtenir [son compte](https://www.strava.com/athletes/1144234183).  
Il [poste un message](https://www.strava.com/athletes/1144234183/posts/46510217) indiquant qu’il va faire une **course**
le **03 juillet** avec une **photo** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image12.png)

Pour retrouver l’endroit de cette image, on peut voir plusieurs éléments intéressants et permettant de réduire fortement
la zone de recherche. Nous recherchons un endroit avec un **panneau stop** (à gauche) proche (moins de 15m) d’une **fontaine pour boire** (à droite).  
En limitant la recherche à la **Haute-Vienne** (comme indiqué dans le post), nous pouvons faire la recherche suivante
sur [*Overpass Turbo*](https://overpass-turbo.eu/) :

```
[out:json][timeout:60]; 
{{geocodeArea:Haute-Vienne}}->.hv; 

nwr[highway=stop](area.hv)->.stop; 
nwr[amenity=drinking_water](area.hv)->.eau; 

nwr.stop(around.eau:15); 
out body; 
>; 
out skel qt;
```

Ce qui permet d’obtenir 7 endroits possibles :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image59.png)

En vérifiant ces différents endroits sur *Google Maps*, on peut obtenir la ville finale : **Saint-Léonard-de-Noblat**.
Le flag est donc : [45.83518223561972, 1.490181515827461](https://maps.app.goo.gl/ajJmZiaotkHeU8sz9).

## Chapitre 1 \- Fait divers \[BONUS\]

### \[BONUS\] L'envol des perroquets

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image149.png)

Une **recherche *Google*** avec les termes de l’énoncé
`En janvier 2023, une convention a rassemblé trois entités françaises dans le cadre d'une mobilisation renforcée pour lutter contre la maltraitance animale`
permet
d’obtenir [un article de la gendarmerie](https://www.gendarmerie.interieur.gouv.fr/gendinfo/actualites/2025/lutte-contre-la-maltraitance-animale-une-mobilisation-renforcee).  
Dans cet article, se trouve la phrase suivante qui donne l’information pertinente : “*Grâce à cette convention, un
réseau de référents spécialisés a été instauré dans les brigades de gendarmerie et les commissariats de police, appuyé
par une politique de formation ambitieuse, co-construite entre la **SPA**, le **MIOM** et le **MASA***“. Le flag est
donc : `MASA_MIOM_SPA`

### \[BONUS\] Le trésor des corbeaux

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image158.png)

Une **recherche *Google*** avec les **mots clés de l’énoncé** `félins naturalisés saisie arras 2026` permet d’obtenir
dans les premiers résultats [le
***Flickr*** de la Douane](https://www.flickr.com/photos/douanefrance/albums/with/72157682738700791). En regardant ce
dernier, on retrouve [l’album de la saisie](https://www.flickr.com/photos/douanefrance/albums/72177720331712030/) sur
lequel on peut voir **3 animaux** différents. Le flag est donc : `3`

### \[BONUS\] L'insouciance du paresseux

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image174.png)

Une **recherche *Google*** avec une partie de la question permet de se mettre sur la bonne voie :
`espèce de mammifère possède la durée la plus courte entre sa découverte par l'Homme et son "extinction"`  
En regardant [un des premiers liens](https://museedesconfluences.fr/fr/le-musee/actualites/la-rhytine-de-steller) sur la
**Rhytine de Steller**, on peut lire la phrase suivante : “*L'animal possède ainsi le record sinistre de l’intervalle de
temps le plus court entre sa découverte et son extinction*“. Le flag est donc : `rhytine de Steller`

## Chapitre 1 \- Petsitter

### La mésange babysitter

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image181.png)

Sur
le [post identifié précédemment](https://www.facebook.com/michelle.sarah2003/posts/pfbid02eroqFYbcZegS1mLgMMj7Mez7bLNgzFKSNECCAgfwuk92hKMy6CwLrHzVQuQT5i3Pl)
avec le **numéro de téléphone** du **petsitter**, un commentaire indique “*un de ses messages sur un autre réseau, avec
son numéro*”. On sait donc que l’on doit chercher son **numéro de téléphone** sur un **autre réseau social**. En
recherchant sur les différents réseaux sociaux, on peut trouver le [compte
*Bluesky* de ce petsitter](https://bsky.app/profile/josphdlmrr.bsky.social) qui nous permet d’obtenir son **pseudo** **“josphdlmrr“** (il faut être **connecté** sur ***Bluesky*** pour que la recherche fonctionne correctement). En
cherchant sur d’autres réseaux sociaux avec ce nouveau pseudo, on peut retrouver [son compte
*Instagram*](https://www.instagram.com/josphdlmrr/) sur lequel il indique son **identité**. Le flag est donc : `Joseph
Delamarre`

### Bavard comme une pie

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image15.png)

En regardant les différents **posts** ***Facebook*** de la **famille Michelle**, nous pouvons
voir [un post de Jean Michelle Jr](https://www.facebook.com/photo?fbid=122105201900982738&set=a.122105202338982738) en
lien avec les animaux auquel **Sarah** et **Lucia** répondent chacune avec une partie de la réponse. Le flag est donc :
`bengal_1200`

### Pris dans la toile

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image58.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image113.png)

Sur le papier communiqué, il y a plusieurs informations intéressantes : on recherche un **bâtiment en construction**, en
lien avec le “zigouigoui” qui ressemble à une **antenne** et son **numéro**. En recherchant `liste antennes france` sur
*Google*, on peut trouver le [site cartoradio de l’ANFR](https://www.cartoradio.fr/#/) qui permet d’arriver sur
le [site open data de l’ANFR](https://data.anfr.fr/accueil). Une recherche sur les antennes avec l’identifiant présent
sur le papier nous
donne [un résultat](https://data.anfr.fr/visualisation/table/?id=observatoire_2g_3g_4g&disjunctive.adm_lb_nom&q=0452750521)
indiquant les coordonnées suivantes : [47°57'3''N 1°53'28''E](https://maps.app.goo.gl/EkHRBGeFPcHHzzqA7). Il nous manque
à utiliser l’élément de **“bâtiment en construction”** qui était présent sur le papier. Or, en vue satellite ainsi qu’en
street view, on peut voir un bâtiment en cours de reconstruction juste en face de la rue :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image137.png)

Un street view en 2026 permet de confirmer que cette zone est bien en travaux. Le flag est
donc : [47.9513141551457, 1.8934234896149447](https://maps.app.goo.gl/UwqTUvFjqjamVHn46)

### Le terrier du lapin

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image68.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image62.png)

En reprenant le compte ***Bluesky*** du **petsitter**, on peut
trouver [une photo](https://bsky.app/profile/josphdlmrr.bsky.social/post/3mkcqcujink2m) qu’il indique avoir prise en bas
de **sa rue**. Il faut donc retrouver cette rue. Pour cela, voici deux axes de recherche :  
Concernant le premier, en regardant la photo, on peut voir en fond **un cours d’eau**. La photo a donc été prise en bord
de **Loire** (le fleuve qui traverse Orléans). En regardant en vue satellite, on peut voir que la **rive nord** semble
être **plus aménagée** que la rive sud, ce qui correspond bien aux **chaises** présentes sur la photo. En faisant en
street view la rive nord, on arrive à retrouver la **mosaïque**
ici : [47.898251811618834, 1.9006543452568465](https://maps.app.goo.gl/qg5h28od6o9a6Az48%20)  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image129.png)

Pour le second axe de recherche, en recherchant directement sur ***Google Image*** la **mosaïque**, on tombe sur une
page [*Decathlon*](https://www.decathlon-outdoor.com/fr-fr/explore/france/street-art-d-orleans-68506b4cbb816) détaillant
un **trajet** sur lequel cette dernière se trouve. Avec l’aide de la **photo**, on peut déterminer qu’elle a été prise
sur **bord de Loire**, et retrouver [l’endroit](https://maps.app.goo.gl/qg5h28od6o9a6Az48%20) grâce au trajet (ou juste
en suivant tout le trajet jusqu’à obtenir le bon endroit).  
En remontant la rue, on peut trouver sur la gauche une **double porte ocre**, correspondant à l’indice noté sur la cage
de Malo, présent dans l’énoncé du challenge :

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image25.png)

Le flag est donc : [47.89882594528582, 1.9004638261852451](https://maps.app.goo.gl/Mfn6tdzcMrAWidqy5)

## Chapitre 2 \- Acte 1

### Tapir dans l'ombre

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image99.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image192.png)

Grâce au **PV d’interrogatoire** disponible en annexe, on sait qu’un individu utilisant le pseudo **Virgata** a contacté
le petsitter via ***Instagram***. En commentaire sur [un post](https://www.instagram.com/p/DWyNL1XDMZR/?img_index=1)
*Instagram* de Joseph, on voit un commentaire signé **Virgata**
par [un compte Instagram](https://www.instagram.com/petosint/) appelé **“petosint”**. En recherchant sur ce pseudo (via [whatsmyname](https://whatsmyname.app/) ou [osintisnotacrime](https://osintisnotacrime.com/app/search) par exemple),
un [compte X](https://x.com/PetOsint) ressort. Sur ce nouveau compte de **PetOsint**, un des
posts [mentionne son 33e anniversaire](https://x.com/PetOsint/status/2038693656106881426) et est daté du **30/03/2026**.
Le flag est donc : `30/03/1993`

### Le Caméléon des internet

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image77.png)

Sur son **compte X**, **Petosint/Virgata**
indique [avoir rejoint des communautés OSINT](https://x.com/PetOsint/status/2053076077291966602). En retournant voir sur
son compte Instagram, on peut constater parmi les différents follows de ce dernier, qu’en plus de nombreux comptes en
lien avec les animaux, il y a le compte de ***Discord France.*** En croisant ces deux informations, on se doute qu’il
faut chercher sur les différentes **communautés OSINT sur *Discord***. Petit indice supplémentaire, en regardant son **image de profil** sur *X*, on voit que celle-ci est **coupée** par le réseau social. Si on regarde l’**image
d’origine**, on peut voir un nouveau pseudo : **“OsintTheAnimals”**  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image160.png)

En allant chercher sur différentes communautés ***Discord*** **OSINT** (*OSINT-FR*, *OscarZulu*, *Osintopia*, etc.) avec
l’un des 2 pseudos, on peut retrouver un [message laissé sur le *Discord* d'*OscarZulu*](https://discord.com/channels/1146816964438798396/1148967737876553808/1501636281602412544) par **PetOsint** (aka **OsintTheAnimals**) :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image133.png)

Un dernier pivot [sur le blog](https://web.archive.org/web/20260711081745/https://blog-de-osinttheanimals.xyz/) indiqué
dans sa bio discord permet de lire [**sa présentation**](https://web.archive.org/web/20260711081858/https://blog-de-osinttheanimals.xyz/presentation/) dans laquelle il donne
son **prénom** et **nom**. Le flag est donc : `Steven Pichon`

### Les piqueboeufs et l'hippopotame

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image8.png)

Sur le **blog de Steven**, en allant voir le **certificat de son site** (soit via un outil externe
comme [web-check](https://web-check.xyz/check/blog-de-osinttheanimals.xyz), soit
en [regardant directement le certificat](https://www.globalsign.com/en/blog/how-to-view-ssl-certificate-details)), on
peut voir que le **certificat** est fait pour **deux noms de domaines** différents, [**into-tacs.shop**](https://web.archive.org/web/20260711082844/https://into-tacs.shop/)
et [blog-de-osinttheanimals.xyz](https://web.archive.org/web/20260711081745/https://blog-de-osinttheanimals.xyz/) :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image7.png)

Le flag est donc : `into-tacs.shop`

## Chapitre 2 \- Acte 2 \- Activités

### La parade du paon

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image155.png)

Sur le [site précédemment identifié](https://web.archive.org/web/20260711082844/https://into-tacs.shop/), on peut voir
les **photos** des différents **membres**. Parmi ces dernières, la photo de **Julietteae** est la seule avec un **nom
différent** de son pseudo indiqué sur le site : elle est nommée avec un autre pseudo **“emmapoirier1990”**  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image80.png)

En recherchant ce **pseudo** sur ***Google***, `”emmapoirier1990”` on peut
trouver [un compte X](https://x.com/EmmaPoirier1990). Ce compte permet de bien confirmer le **prénom** et le **nom** de
**Julietteae**. Le flag est donc : `Emma Poirier`

### Les Traces de l'Ours

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image97.png)

À partir du [compte X d’Emma](https://x.com/EmmaPoirier1990), on peut accéder aux **listes qu’elle a créées**, mais
aussi aux **listes auxquelles elle appartient** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image40.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image88.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image116.png)

Dans [cette liste](https://x.com/i/lists/2030953833291997356), il y a **deux autres individus** :
le [créateur de la liste](https://x.com/lebriochard69) dont la photo de profil ressemble à **Martinezi**, ainsi
que [MorelHunt](https://x.com/MorelHunt25591) dont la **biographie** indique que son véritable pseudo est **Morelos**.
Ici, on doit se concentrer sur **Morelos**. Sur son fil *Twitter*, on peut voir plusieurs **posts *9gag*** récents, ce
qui permet de se concentrer sur cet aspect. En allant voir sur ***9gag*** le **format URL des profils**, on voit que
celle-ci est formée de la manière suivante *https://9gag.com/u/pseudo_de_la_personne*. En remplaçant le nom
d’utilisateur par les pseudos connus de **Morelos**, on parvient à
trouver [son compte 9gag](https://9gag.com/u/morelhunt) qui contient un **lien *Pastebin*** dans sa **biographie** : [https://pastebin.com/YBwuJjLP](https://pastebin.com/YBwuJjLP). Sur ce ***Pastebin***, on apprend son **identité**.
Le flag est donc : `Hubert LeMaitre`

### La chasse du guépard

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image196.png)
Le début de la résolution est la même que [les traces de l’ours](#les-traces-de-lours). Une fois
identifié [le compte X de Martinezi](https://x.com/lebriochard69), nous avons un nouveau pseudo : **lebriochard69**. En
recherchant sur ce pseudo via des outils
spécialisés ([RhinoUserCheck](https://github.com/degun-osint/RhinoUserChecker), [Maigret](https://github.com/soxoj/maigret)), [un compte
*Twitch*](https://www.twitch.tv/lebriochard69) ressort. La réponse se trouve dans sa **biographie** *Twitch*. Le flag
est donc : `Edouard Pasquier`

### Les Abysses des Lophiiformes

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image67.png)

En reprenant [le *Pastebin* de Morelos](https://pastebin.com/YBwuJjLP) obtenu précédemment, on obtient un morceau
d’URL : **/c3e5e2b5e8d159cd4c02a4684a376c494418beafa24ef31e5837f**  
**d8101b0b1ca.html**. Le seul site lié à **Morelos** étant **into-tacs**, si on ajoute ce morceau d’URL à la suite de
celui du site, on parvient
sur [une page nécessitant un mot de passe](https://web.archive.org/web/20260711101201/https://into-tacs.shop/c3e5e2b5e8d159cd4c02a4684a376c494418beafa24ef31e5837fd8101b0b1ca.html) :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image173.png)

Il nous faut donc le **mot de passe** pour accéder à cette page. Sur [le
*Twitch* de Martinezi](https://www.twitch.tv/lebriochard69/videos) vu précédemment, il y a plusieurs **vidéos**,
dont [une vidéo](https://www.twitch.tv/videos/2802852167?collection=trJomqhPohiBrQ) qui contient lors des premières
secondes de visionnage un **“MDP ONION”** : **“ulysse”**  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image46.png)

En utilisant ce **mot de passe** sur la **page précédemment obtenue**, on peut accéder au lien du **site onion** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image66.png)

Le flag est donc : `2mflu6auogvubqrf2pv4jzsaaacs6k2mf5vfn5evstgdo6f6ydcvckad.onion`

## Chapitre 2 \- Acte 2 \- Droit

### \[BONUS\] Les fourberies du renard

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image156.png)

En fouillant sur [le site d’into-tacs](https://web.archive.org/web/20260711082844/https://into-tacs.shop/), dans la
partie [**mentions légale**](https://web.archive.org/web/20260711082913/https://into-tacs.shop/mentions-legales.html),
on peut voir une mention sur un **certificat de capacité de dressage au mordant non rempli**. Un commentaire dans le
code source précise :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image126.png)

Cependant, sur la page d’accueil du site, une **photo** montre déjà l’**utilisation de ce type de matériel** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image28.png)

Une **recherche *Google*** permet de trouver les premières mentions des articles concernés :
`article loi certificat mordant`. En creusant, on comprend que l’article **encadrant** le **dressage au mordant** est
l’article
suivant : [https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031281823](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031281823).
Dans la partie **“voir les versions”** de l’article, on peut accéder au **détail** des versions, et voir la **date**
depuis laquelle le texte actuel est en vigueur. Le flag est donc : `Article L211-17 du Code rural et de la pêche
maritime-01/01/2016`

### Le loup déguisé

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image177.png)

Sur le [site d’into-tacs](https://web.archive.org/web/20260711082844/https://into-tacs.shop/), dans la **FAQ**, il est
fait mention d’un certain **“Maître Artaux”** qui s’occupe de gérer les litiges juridiques :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image47.png)

Pour le retrouver, on se dirige vers le réseau professionnel le plus utilisé : ***LinkedIn***. Une recherche avec **“Artaux”** dans le secteur d’activité **“cabinet d’avocat”** fait
ressortir [un profil](https://www.linkedin.com/in/james-artaux-a502b83ba/) :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image139.png)

Dans sa **biographie**, il fait mention de **partenariats** avec des entreprises **“dans le domaine de la sécurité
privée et l'élevage canin”** ce qui confirme bien le lien avec into-tacs. Le flag est donc : `James Artaux`

### Les commencements de l'oiseau

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image131.png)

A partir de l’identité de **James Artaux**, une **recherche *Google*** `James Artaux` permet d’accéder à [son compte
*Facebook*](https://www.facebook.com/people/James-Artaux/61582170877792/). Dans sa **biographie**, il précise son **pseudo**. Le flag est donc : `Tigris`

### Le Territoire du Loup

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image35.png)

A partir du [compte *Facebook* de James](https://www.facebook.com/profile.php?id=61582170877792), on
voit [un post](https://www.facebook.com/permalink.php?story_fbid=pfbid0r8yh9yztmQkeXfBdp9mkqt1YkZRV5GWvbSbeJjmdnL3yRMWq2j7XRjGzeycTRYsel&id=61582170877792)
indiquant qu’il **vend son échiquier en bois**. Il utilise probablement ***Facebook Marketplace*** pour vendre son
échiquier,
or, [un article sur le blog de Steven](https://web.archive.org/web/20260711081908/https://blog-de-osinttheanimals.xyz/posts/facebook-marketplace-bug/)
donne un **indice** sur **comment accéder au profil marketplace** de James :

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image130.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image128.png)

En suivant cette procédure (aller sur le profil marketplace en étant déconnecté), on parvient à
obtenir [la liste des objets](https://www.facebook.com/marketplace/profile/61582170877792) qu’il vend. Plusieurs objets
ont été pris en **photo en extérieur** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image150.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image194.png)

Or,
dans [un post](https://www.facebook.com/permalink.php?story_fbid=pfbid0r8yh9yztmQkeXfBdp9mkqt1YkZRV5GWvbSbeJjmdnL3yRMWq2j7XRjGzeycTRYsel&id=61582170877792)
***Facebook***, il indique qu’il a dû **sortir de son jardin** pour prendre certaines photos, donc ces dernières doivent
être prises **juste à côté de chez lui**. En concentrant la recherche image sur le **haut de la tour**, on obtient
plusieurs résultats en lien avec un **“télégraphe Chappe”** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image79.png)

En recherchant la liste des **télégraphes Chappe**, on trouve une liste disponible
sur [wikimédia](https://commons.wikimedia.org/wiki/Category:Chappe_towers_in_France) avec des
photos, [dont une](https://commons.wikimedia.org/wiki/File:T%C3%A9l%C3%A9graphe_Chappe_-_panoramio.jpg) qui ressemble
fortement à l’image que l’on a, avec une **église** juste à côté. Cette photo est geotaggée à **Baccon** (45), proche
d’Orléans. Afin de confirmer exactement de quelle maison il s’agit, on s’appuie
sur [un post](https://www.facebook.com/permalink.php?story_fbid=pfbid0dmo7iJJ21J7EAh9UhL8yjupmvn8C3bXzxcMYuogLowQnD8B47iAKoaYmzz2ZZEpwl&id=61582170877792)
***Facebook*** de **James** qui indique **habiter au numéro 89 de sa rue**. Le flag est
donc : [47.89203480716773, 1.628970214089361](https://maps.app.goo.gl/wDVz1uNBXvpMAePa9)

## Chapitre 2 \- Acte 2 \- Développement

### La Mémoire de l'Éléphant

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image191.png)

A partir des différents **sites web** identifiés plus
tôt ([into-tacs.shop](https://web.archive.org/web/20260711082844/https://into-tacs.shop/)
et [le blog de Steven](https://web.archive.org/web/20260711081745/https://blog-de-osinttheanimals.xyz/)), on va faire
une [requête rdap](https://lookup.icann.org/en) (rdap est le remplaçant de whois) pour récupérer les informations sur
les noms de domaines (les deux renvoient plus ou moins le même résultat, à l’exception que le serveur rdap pour les
`.shop` a un peu de mal à répondre). On obtient ainsi les **informations** sur la **personne** ayant loué le nom de
domaine :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image6.png)

Le flag est donc : `Dave Renault`

### Le Nid Douillet

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image26.png)

A partir du prénom et du nom identifiés précédemment, une recherche avec  `Dave Renault` sur l’un des outils les plus
appréciés des développeurs s’impose : ***Github***. Une fois son compte trouvé,
sur [son README](https://github.com/RenDavePet), on peut confirmer qu’il a bien **travaillé** avec **into-tacs**. Pour
identifier son **adresse mail personnelle**, on va se concentrer sur ses **commits** pour voir s’il n’a pas configuré
son git pour inclure son adresse mail. En prenant par exemple le **premier commit** de son **README** et en **ajoutant
.patch à l’URL**, on obtient
la [version raw du commit](https://github.com/RenDavePet/RenDavePet/commit/06169761a4b3fa60799744ae5f1b74e74dd636c8.patch)
qui contient les informations techniques, comme son **adresse mail**. Le flag est donc : `RenDavePet@proton.me`

### \[BONUS\] La Fourmilière d'Informations

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image72.png)

Sur le compte ***Github*** de **Dave Renault**, on peut voir que celui-ci a **fork** [un projet en lien avec
*Wikipédia*](https://github.com/RenDavePet/Wikipedia). Une **recherche *Google*** avec son **pseudo** `RenDavePet` fait
ressortir directement des liens ***Wikipédia***.  
En fouillant sur la [page de Baccon](https://en.wikipedia.org/w/index.php?title=Baccon&action=history) où son pseudo
ressort, on parvient à retrouver [son compte *Wikipédia*](https://en.wikipedia.org/wiki/User:RenDavePet) dans les
éditeurs récents (via l’historique de la page) où il indique bien être **développeur**. Il a
ajouté [une image d’une tour Chappe à Baccon](https://commons.wikimedia.org/wiki/File:Chappe_tower.jpg) en laissant les
**métadonnées**. Le flag est donc : `Google Pixel 8`

## Chapitre 2 \- Acte 3 \- Communication

### La danse des abeilles

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image16.png)

A partir [du site onion identifié](http://2mflu6auogvubqrf2pv4jzsaaacs6k2mf5vfn5evstgdo6f6ydcvckad.onion/)
précédemment (une archive zip est disponible en annexe, néanmoins les scripts ne sont pas fonctionnels), dans l’onglet **contact**, on peut voir que le groupe semble utiliser ***Keybase*** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image73.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image11.png)

En cherchant n’importe quel **pseudo** identifié précédemment sur *Keybase*, on tombe sur des comptes en lien avec
l’équipe **“lameuterouge”** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image102.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image33.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image49.png)

En créant un compte ***Keybase***, il est possible de **rejoindre l’équipe publique**. Dans le salon **#Events**, **Lycaon** envoi un message indiquant les **informations** pour une **soirée de rencontre et de récupération** **des
besoins** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image87.png)

Le flag est donc : `amanra_31/05/2026`

### L'Instinct du Pigeon Voyageur

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image52.png)

Sur le ***Keybase*** de **LaMeuteRouge**, **Uncia** indique qu’elle a déposé “*les points de départ pour la soirée dans
la BAL morte* *\[...\]* *pendant une course*”. Le réseau social le plus connu de course est ***Strava***. Une recherche
par pseudo avec **“uncia”** sur [Sherlock](https://github.com/sherlock-project/sherlock)
ou [Maigret](https://github.com/soxoj/maigret) permet d’obtenir justement [un compte
*Strava*](https://www.strava.com/athletes/uncia) au nom de **Marisa Giraud** dont l’image de profil montre la même
personne que son image *Keybase*. Or, on sait que durant ses courses, elle passe à la boîte aux lettres morte. Sur
*Strava*, il est possible de **télécharger les GPX**, pour ensuite les réimporter **tous les 5** sur une même carte (avec [https://gpx.studio/app](https://gpx.studio/app) par exemple) pour identifier le lieu de **passage commun** à
toutes ses courses :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image19.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image122.png)

En regardant cet endroit de plus près en **street view**, on constate qu’il y a une **table**, comme précisé dans un **autre message sur *Keybase*** dans le salon **\#general** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image2.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image143.png)

Le flag est donc : [47.90727265298383, 1.910894038164717](https://maps.app.goo.gl/eZLsbYoxpLGa2uZT6)

### \[BONUS\] Le Mille Pattes

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image152.png)

Sur ***Keybase***, dans le salon **\#membres-uniquement**, **Uncia** poste un **message** en lien avec les **rencontres
de fournisseurs** qu’elle réalise pendant ses randonnées, ainsi qu’un lien vers ***AllTrails*** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image175.png)

En se créant un compte sur ***AllTrails***, on peut accéder à l’onglet **communauté** sur lequel on peut rechercher **uncia** ce qui fait ressortir [son compte](https://www.alltrails.com/fr/members/uncia-giraud) :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image65.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image172.png)

Sur son profil, on peut voir **plusieurs randonnées** qui ont été faites par Uncia dont 2 avec un **GPX**. On télécharge
ces 2 GPX pour mieux les analyser. Sur la page
d’[une des randonnées](https://www.alltrails.com/explore/recording/cala-portinatx-sa-descoberta-892dedf) avec un GPX, **Uncia** indique que “*Il y a même des endroits pour manger tranquillement avec plusieurs personnes*”, ce qui pourrait
correspondre avec une **rencontre avec un fournisseur**. De plus, sur cette randonnée, la durée de déplacement et la
durée totale présentent un delta d’**une heure** contrairement à l’autre randonnée :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image132.png)

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image179.png)

En exportant le fichier GPX (les trois points \> export route file \> GPX track) et en le visualisant sur un **viewer** (comme [mygpsfiles.com](https://www.mygpsfiles.com/app/)), on peut constater une **pause** dans un **bâtiment** (en
modifiant le graph pour indiquer la distance en fonction du temps) :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image121.png)

La pause a donc eu lieu dans ce bâtiment. De plus, sur
le [calendrier de Maximus](https://calendar.google.com/calendar/newembed?src=tuskontheroad@tacosint.fr) obtenu grâce au
**compte** ***Google*** de son **adresse mail**, on peut confirmer qu’**Uncia** a bien rencontré un fournisseur le **17/03/2026** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image198.png)

Le flag est donc : [39.10713268794036, 1.5363382879599912](https://maps.app.goo.gl/tPg9EwbafGPY5t7TA)

## Chapitre 2 \- Acte 3 \- Financement

### L'Épine de l'Oursin

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image159.png)

Ce challenge a juste pour objectif de donner l’adresse crypto de départ “0x3D8B1dAc8556a66c2A2280eaAA153C9b026e2585” aux
joueurs. Le flag est donc : `Merci Péhuson`

### La Pieuvre et ses Tentacules

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image112.png)

A partir du ***Keybase***, on sait que **Leo** a **leak** sur ***Facebook*** une **adresse crypto** utilisée pour
émettre **un unique paiement** :  

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/image120.png)

*En annexe pour mieux détailler les échanges, il y a un graph [ZeroNeurone](https://zeroneurone.com/) avec un onglet
spécifique qui récapitule les **transactions cryptos**.*
Pour résumer cela, il fallait bien remonter **toutes les transactions** jusqu’à arriver soit à une “impasse” (pas de
transactions depuis l’adresse identifiée), soit à l’adresse *0x6cc9397c3b38739dacbfaa68ead5f5d77ba5f455* qui est
un [faucet permettant d’obtenir des fonds sur un testnet](https://sepolia-faucet.pk910.de/). Les recherches sur les
transactions peuvent se faire via un explorateur comme [etherscan](https://etherscan.io/) en précisant bien
le [testnet sepolia](https://sepolia.etherscan.io/).  
On peut donc isoler les adresses cryptos suivantes qui n’ont effectué **qu’une transaction** :

- 0x2fce52CB97292DEbFea77F8C8ED489a9c3545b78
- 0x5EE9C58349Be35a453284288a885f382038C439A
- 0x3D8B1dAc8556a66c2A2280eaAA153C9b026e2585 (paiement petsitter)
- 0xB9b36D66571bEc871268d95D7Aa482aC9a09757a (client)
- 0xBf4a51C381573C9CAf58C9Dd49c8f9ab246Ba1e6 (client)

En cherchant ces adresses crypto sur *Facebook* **et en coc

---

# File: README.md

# Write-up TACOSINT - L'appel de la forêt 2026 - OSINT CTF

### By Eldwiin & Kipixelle & R0ck3t & Tab & Zmondy - Team Tacosint

![](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Images/Affiche.jpg)

# L'appel de la foret
## CTF
L’appel de la forêt est un CTF 100% OSINT, se déroulant en ligne, avec une partie compétitive du 03 juillet 20h00 CET (UTC+1) au 09 juillet 2026 20h00 CET (UTC+1). Créé par l’association Tacosint, il a comme partenaires Badgeforge, OscarZulu et EPIEOS.
Tacosint est composée des membres suivants :
- Eldwiin
- Kipixelle
- R0ck3t
- Tab
- Zmondy

## Remerciements
Nous souhaiterions remercier toutes les personnes qui nous ont accompagnés lors de la création de ce CTF !
- **[BadgeForge](https://www.badgeforge.eu/)**, **[Oscar Zulu](https://oscarzulu.org/)**, **[EPIEOS](https://epieos.com/)**, nos sponsors et fournisseurs des lots ;
- **[ElueTime](https://eluetime.carrd.co/)**, notre super graphiste, pour la création du logo, des emotes, ainsi que des badges ;
- **[Oscar Zulu](https://oscarzulu.org/)** et **[Boosty](https://github.com/0SINTER)** pour leurs conseils sur la création du CTF ;
- **[Oscar Zulu](https://oscarzulu.org/)** et **[Hack'olyte](https://hackolyte.fr/)** pour les plugins sur le CTFd ;
- Nos **betatesteurs** et personnes qui nous ont supportés tout au long de la création du CTF ;
- **Les joueurs** pour leur persévérance et leur bonne humeur durant ce CTF.


# Write-up
## Markdown
  - [Write-up](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Writeup.md)
## PDF
  - [Write-up](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Writeup.pdf)
## Zeroneurone
  - [Lien de l'outil](https://zeroneurone.com/)
  - [Le zip à importer dans Zeroneurone](https://github.com/Tacosint/Write-up_L-appel-de-la-foret_2026/blob/main/Zeroneurone.zip)
