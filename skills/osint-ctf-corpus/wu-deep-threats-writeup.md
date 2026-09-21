# Deep Threats — Write-up officiel (PDF)

Source: write-up PDF « Deep Threats - Write-up » (Correction des challenges), auteur Deep Threats.  
Importé dans le corpus Hermes depuis un export iLovePDF (lien de téléchargement éphémère — contenu archivé ici).  
Métadonnées PDF: Title=`Deep Threats - Write-up`, Subject=`Correction des challenges`, Producer=iLovePDF.

> Flags / réponses d’**autres** CTF = exemples de **méthodo** uniquement.  
> Pour un CTF en cours: corréler ≥2 sources; ne jamais submit sans OK humain/team.

---

PRÉSIDENT
Question : Avant d'entrer chez Marinatech, quelle était la fonction qu'occupait son Président ?  
Une recherche sur Marinatech Industries permet d’identifier son dirigeant, Marc-Olivier 
Chasseneuil. Son profil LinkedIn constitue alors le pivot principal du challenge : en consultant 
ses informations professionnelles, on retrouve la fonction qu’il occupait avant d’intégrer 
l’entreprise Marinatech. 
🚩 Flag : ingénieur naval
UN SOUPÇON DE SOUPÇON
Question : Depuis quand cet employé s'interroge-t-il sur la situation de son entreprise ?
Le site de Marinatech Industries permet d’identifier Enzo Riesmeyer parmi les employés de 
l’entreprise. Son nom constitue le premier pivot : une recherche sur les réseaux sociaux permet 
de retrouver son compte X. En remontant ses publications, on découvre le premier post dans 
lequel Enzo commence à faire part de ses inquiétudes. La date de cette publication fournit 
directement la réponse au challenge.
🚩 Flag : 30/05/2026

UN NOUVEL ALLIÉ
Question : À quelle date Marinatech a-t-elle signé ce partenariat ?
Le profil LinkedIn de Marc-Olivier Chasseneuil permet de repérer une publication annonçant un 
nouveau partenariat destiné à accompagner le développement international de Marinatech et sa 
stratégie commerciale. Le nom du partenaire constitue alors le pivot vers le site d’AquaVentis, où 
les actualités permettent de retrouver l’annonce officielle du partenariat ainsi que sa date de 
signature.
🚩 Flag : 20/05/2026
WESH COUZ T’ES OU ?
Question : Quel est le nom du lieu visible à gauche sur la photo qu'il a partagée et dans quel pays 
se trouve ce lieu ? 
Sur son compte X, Enzo Riesmeyer fait part de son inquiétude concernant la disparition de son 
cousin et publie la dernière photo qu’il a reçue de lui. L’objectif est alors de géolocaliser cette 
image. Le principal indice se trouve sur une pancarte visible à l’arrière-plan : en ouvrant 
simplement la photo en plein format dans un nouvel onglet, son inscription devient lisible et 
permet d’identifier Mandaue Assembly of God International. Une recherche sur ce nom 
permet ensuite de localiser le lieu aux Philippines.
🚩 Flag : Mandaue Assembly of God International_Philippines

UN PORTEFEUILLE BIEN GARNI
Question : Combien d'autres entreprises AquaVentis accompagne-t-elle en plus de Marinatech ?
En poursuivant les recherches sur AquaVentis, la page d’accueil de son site présente un 
carrousel regroupant les entreprises de son portefeuille. Il est possible de les compter 
directement à l’écran, mais le défilement rend la méthode assez propice aux erreurs. Une 
solution plus fiable consiste à consulter le code source de la page, dans lequel la liste complète 
des entreprises affichées dans le carrousel peut être retrouvée et comptabilisée.
🚩 Flag : 23
L’ÉCOLO
Question : Pouvez-vous retrouver l'identité réelle de celui qui a diffusé l'information ?  
À la suite de la fuite concernant l’utilisation du tributylétain, Enzo ne livre qu’un indice sur son 
auteur : le pseudonyme « Tang Bordel ». Une recherche permet de retrouver le compte 
Tang_Bordel sur X et la publication à l’origine de la fuite. Les informations présentes sur ce profil 
et en particulier son username, @Tang_Bordel permettent ensuite de pivoter vers son compte 
Mastodon. En remontant dans les archives de ce dernier avec la Wayback Machine, à la période 
de création du compte, une ancienne version du profil révèle l’identité qui se cache derrière le 
pseudonyme.
🚩 Flag : Tanguy Bordelier

DEAL
Question : Quel est l'identifiant du moyen utilisé pour payer Tanguy ?
Le compte de Tanguy constitue ici votre premier pivot. À partir de son profil, récupérez l'adresse 
de son wallet puis consultez-la sur l'explorateur de la blockchain Sepolia, Etherscan. L'historique 
des transactions permet d'identifier le wallet qui a servi à le 
rémunérer.https://sepolia.etherscan.io/address/0xCb1e8E1E6794349E18593dB17F9C7DB9948c64
45
🚩   Flag :
0 188 7 50 72 0 2 327425 1 784428 260x E f B A E cBFb D cFe f
UN COIN DISCRET
Question : Indiquez l’identité du payeur ainsi que la référence figurant sur l’élément ayant permis 
son identification.
Reprenez le wallet ayant servi à payer Tanguy et examinez son historique. Vous y repérez une 
transaction entrante provenant d'un autre portefeuille : ce nouveau wallet devient votre pivot.

Ouvrez les détails de cette transaction sur Etherscan et examinez les informations qui lui sont 
associées. Un commentaire permet d'identifier l'entité à l'origine du versement ainsi qu'une 
référence caractéristique. Ces deux éléments composent le flag attendu.
https://sepolia.etherscan.io/tx/
0x16429492f59af17bf557e55467c59a5f75303d1ab1e541f6c8b29cbdd0f09079

🚩 Flag : Institut Lotus_APT509
DOCTOR WHO
Question : Pouvez-vous trouver l'acronyme de cette université et quel est son laboratoire de 
rattachement ? 
L’identité de Wuan Xijiang étant désormais connue, le site de Marinatech Industries permet 
d’identifier l’université partenaire dans laquelle il réalise ses travaux : l’Université Atlantique de 
Lorient (UAL). 
Sur le site de l’université, l’onglet consacré à la formation donne accès au calendrier des 
soutenances de thèses. En recherchant Wuan dans ce calendrier, sa soutenance permet de 
retrouver le laboratoire auquel il est rattaché, le LCMF.

🚩 Flag : UAL_LCMF
WUAN UPON A TIME
Question : Pouvez-vous trouver dans quelle université il a fait ses études avant d'arriver à l'UAL et 
chez Marinatech ? 
Pour retrouver l’université d’origine de Wuan Xijiang au Lianhua, il faut cette fois s’intéresser à 
sa présence sur les réseaux sociaux. Une recherche sur son identité permet de retrouver son 
compte Reddit. Parmi ses publications, Wuan évoque lui-même son parcours et mentionne la 
LUMS, fournissant ainsi le nom complet de son université d’origine.

🚩 Flag : Lianhua University for Marine Sciences
PAS D’AMI COMME TOI
Question : Qui semble être la personne la plus influente dans son entourage et pouvez-vous 
trouver des éléments sur lui comme son adresse mail personnelle par exemple ? 
Pour identifier la personne susceptible d’avoir exercé une influence sur Wuan Xijiang, il faut 
s’intéresser à celui qu’il présente comme son mentor. Wuan partage un document de ce dernier 
sur son compte Reddit ou, alternativement, sur son profil Medium. En ouvrant le document 
Google Docs puis l’interface de demande de partage, sans envoyer la demande, il est possible 
de voir l’adresse e-mail associée à son auteur. Celle-ci fournit un nouveau pivot grâce au 
pseudonyme Zhouwenj71.
Les recherches sur le Lianhua permettent ensuite de découvrir son wiki et l’existence du réseau 
social Qiao. Une recherche de Zhouwenj71 sur cette plateforme permet enfin de retrouver le 
profil correspondant et de révéler l’identité complète du mentor de Wuan. 
 
🚩 Flag : Zhou Wenjie
GEOGUESSR LEVEL 1
Question : Quelle est la capitale du Lianhua ?
Les recherches s’orientent désormais vers la République du Lianhua. Une simple recherche sur 
le pays permet de retrouver son wiki, qui rassemble les principales informations géographiques 
et institutionnelles le concernant. La consultation de la fiche consacrée au Lianhua permet 
directement d’identifier sa capitale.
🚩 Flag : Xinhai

METAL HURLANT 
Question : Quel est le numéro atomique du Lantrium ?
Les recherches sur le Lianhua conduisent naturellement à s’intéresser au Lantrium, un élément 
qui apparaît à plusieurs reprises dans l’environnement du pays. Le wiki du Lianhua comporte une 
page spécifiquement consacrée à ce matériau. Sa fiche fournit directement ses principales 
caractéristiques, parmi lesquelles son numéro atomique.
🚩 Flag : 128
COURRIER INDÉSIRABLE 1/2
Question : Quelle est l'adresse IP de l'émetteur ?
Vous disposez du mail de menaces reçu par Enzo, mais l’information recherchée n’apparaît pas 
directement dans le message. Depuis le menu du mail, sélectionnez « Afficher l’original » afin 
d’accéder à son header complet et aux différentes données techniques liées à son 
acheminement. L’examen de ces en-têtes vous permet notamment d’identifier l’adresse IP utilisée 
par l’expéditeur.

🚩 Flag : 47.242.108.213
FRENCH TOUCH
Question :  Quel est le premier domaine dans lequel la France est reconnue pour son expertise 
selon l'auteur d'un article au Lianhua ?
Sur le site du Lianhua News Network (LNN), recherchez l’article « Hydronix Marine Corporation 
Strengthens Commitment to Maritime Innovation with LORII Investment ». Sa lecture vous 
permet d’identifier le premier domaine dans lequel la France est reconnue pour son expertise.
🚩 Flag : Naval architecture
UNE BELLE HISTOIRE
Question : Pour combien de temps le partenariat entre AquaVentis et Hydronix a-t-il été signé et 
quel est l'acronyme du nom exact de la structure concernée par celui-ci ?

Pour retracer ce partenariat, rendez-vous sur le site de LNN (lianhuanews-network.info) et 
visionnez la vidéo consacrée à l’accord conclu entre AquaVentis et Hydronix. Celle-ci vous 
permet d’identifier directement sa durée de cinq ans et mentionne également un centre 
d’innovation maritime situé à Haidong. Ce lieu constitue votre second pivot : en consultant la 
page du wiki consacrée à Haidong, vous pouvez retrouver le nom exact de cette structure et son 
acronyme, LORII. 
🚩 Flag : 5 ans_LORII
ÇA C’EST DE LA DOCTRINE
Question : En matière d'innovation, que conclut l’auteur du rapport sur l'utilisation du Lantrium ?
La page du wiki consacrée au Lantrium constitue votre point de départ. En consultant les 
références qui y sont citées, vous découvrez l’existence de l’Institut Lotus ainsi que d’un rapport 
consacré au Lantrium. Rendez-vous alors sur le site de l’Institut pour retrouver ce document. La 
réponse se trouve au chapitre 7, consacré aux principes définis par l’auteur : le passage relatif à 
l’innovation précise ce que chaque exportation de Lantrium devrait apporter au Lianhua.
🚩 Flag : Chaque kilogramme de Lantrium exporté devrait contribuer à l'acquisition d'un 
savoir, d'une technologie ou d'une capacité industrielle nouvelle au bénéfice du Lianhua.
TABLEAU DE CHASSE
Question : Dans l’un de ses rapports, combien d’entreprises font l’objet de l’attention de l’institut 
Lotus ? 
Rendez-vous sur le site de l’Institut Lotus et recherchez le rapport intitulé « Conformité 
environnementale des fournisseurs du secteur naval : quels risques pour les chaînes 
d'approvisionnement stratégiques ? », rédigé par Lucy Wong. La lecture du document vous 
permet d’identifier les différentes entreprises auxquelles l’autrice fait référence dans son analyse. 
Il ne vous reste alors plus qu’à les comptabiliser pour obtenir la réponse attendue.
🚩 Flag : 4

LA PLUME ET LE POUVOIR
Question : Quelle fonction l’autrice de la majorité des publications joue-t-elle au sein de l’Institut 
Lotus ?
Commencez par parcourir les différentes publications de l’Institut Lotus et intéressez-vous à 
leurs auteurs. Vous constaterez que Cheryl Lin est à l’origine de la majorité d’entre elles. Son 
identité devient alors votre pivot : rendez-vous sur la page Gouvernance du site de l’Institut, où 
sont présentés ses principaux membres et leurs responsabilités. Vous y retrouverez la fonction 
exacte occupée par Cheryl Lin.
🚩 Flag : Directrice des relations publiques et des partenariats stratégiques
UN VISAGE FAMILIER 
Question : Quel est le nom complet de Cheryl Lin ? 
Une femme ressemblant fortement à Cheryl Lin apparaît sur une publication LinkedIn de 
Jérôme Osfart. La ressemblance constitue un indice, mais elle ne suffit pas à établir 
formellement son identité. Pour obtenir une confirmation, utilisez la Wayback Machine afin de 
consulter d’anciennes versions du site de l’Institut Lotus. Vous découvrirez qu’elle apparaissait 
auparavant sur le site sous une forme plus complète de son nom, incluant son nom d’épouse.

🚩 Flag : Cheryl Lin Osfart
THE CREATOR
Question : Qui est le créateur du site de l’Institut Lotus ? 
Pour identifier le créateur du site de l’Institut Lotus, intéressez-vous aux informations laissées 
par le CMS. En ajoutant le paramètre /?author= à l’URL du site, vous pouvez énumérer les 
différents comptes auteurs en faisant varier l’identifiant. En poursuivant jusqu’à /?author=5, le 
site vous redirige vers le profil correspondant et révèle l’identité de la personne à l’origine de sa 
création.
🚩 Flag : Liam Rong
JARDINIER ANONYME
Question : Pouvez-vous déterminer à quelle entité Liam Rong est rattaché et le lien qui l'unit à 
celui auquel vous pensez ?

L’identité de Liam Rong étant désormais connue, recherchez son profil sur le réseau social Qiao, 
où il utilise le pseudonyme Rongbrother1. Sa section « À propos » permet d’identifier 
directement son employeur, le Ministère de la Recherche et de l’Innovation. Sa liste d’amis 
fournit le second élément recherché : vous y retrouvez Chen Rong, dont le pseudonyme 
Rongbrother2 permet de déduire le lien de parenté entre les deux hommes.
Selon l’outil de traduction utilisé, l’employeur de Liam pouvait apparaître comme « Ministère » 
ou « Département de la Recherche et de l’Innovation » : les deux formulations étaient donc 
acceptées.
🚩 Flag : Ministère de la recherche et de l'innovation_frère
À TABLE !
Question : Quel est le nom du restaurant et à quelle grande catégorie d'institution appartiennent 
les bâtiments officiels situés juste en face ?
Sur le profil Qiao de Cheryl, vous trouvez une publication dans laquelle elle explique être de 
retour au pays et attendre un ami pour déjeuner devant son restaurant favori.
Le wiki du Lianhua référence un outil de cartographie réalisé par un internaute, lna.maps.space. 
Recherchez une place correspondant aux éléments visibles sur la photo : une fontaine, des 
arbres et plusieurs bâtiments en arrière-plan. La configuration permet d’identifier le restaurant. 
En face se trouvent trois bâtiments administratifs dont l’entité commune est le gouvernement.

🚩 Flag : Bob Presidential Restaurant_government
Y A ANGUILLE SOUS PÉTALE
Question : Quelle interface pourrait se cacher derrière la façade de l’Institut Lotus ?
Pour découvrir la partie cachée de l’Institut Lotus, commencez par rechercher l’adresse IP 
associée à son site web, à l’aide d’un service tel que Mon-IP. 
Utilisez ensuite cette adresse comme pivot dans un moteur d’analyse d’infrastructures exposées 
tel que Shodan ou Censys. Les informations associées à l’hôte vous permettent de retrouver, en 
bas des résultats, une adresse .onion liée à l’Institut Lotus.
🚩 Flag : v6bo7dfnuvlyha3zfmftozjihp4kog3qdpzhkmcog5akpzm6i3yhlmad.onion

SÉSAME OUVRE-TOI
Question : Quel est le nom de l'espace que vous découvrez derrière le .onion ?
L’énoncé vous invite à vous intéresser aux membres de l’Institut Lotus suffisamment haut placés 
pour disposer d’un accès à l’interface cachée. Retournez donc sur le profil Qiao de Cheryl Lin et 
observez attentivement ses publications. Sur l’une de ses photos, Cheryl pose devant son bureau 
et un post-it placé sous son écran laisse apparaître une suite de nombres. En soumettant cette 
suite à un outil de décodage (comme dcode.fr)  vous pouvez identifier un encodage ASCII qui, 
une fois converti, révèle le mot de passe. 
Reste l’identifiant : nul besoin de chercher beaucoup plus loin, puisqu’il correspond tout 
simplement au nom d’utilisateur de Cheryl sur Qiao. Ces deux informations vous permettent 
de vous authentifier sur l’interface cachée de l’Institut et d’accéder à son contenu.
🚩 Flag : Black Lotus
UN HOMME OCCUPÉ
Question : À quelle entité appartient Zhou Wenjie et quelle est sa fonction officielle ?
Une fois connecté au réseau du Lianhua, rendez-vous sur le site du gouvernement (gouv.ln). 
Dans la section « Gouvernement », qui présente les différents acteurs institutionnels du pays, 
recherchez Zhou Wenjie. Sa fiche vous permet d’identifier à la fois l’entité à laquelle il appartient 
et sa fonction officielle.
 Flag : National Innovation Council_Director🚩
CONTRÔLE TOTAL
Question : Quelle est la référence de cet article ?

Maintenant que vous avez accès à l’internet du Lianhua, consultez les bases de données 
gouvernementales. Dans la base consacrée aux lois, recherchez le « Strategic Minerals and 
Materials Act of the Republic of Lianhua ». L’article 15 de cette loi contient une section 
spécifiquement consacrée au Lantrium et fournit la référence attendue.
 Flag : LH-ENE-2026-082 - Art. 15🚩
MADE IN FRANCE
Question : Quel est l'identifiant du brevet déposé dans la base de données nationale avec la 
technologie de Marinatech ?
Rendez-vous tout d’abord sur la base de données nationale des brevets du Lianhua.
Recherchez ensuite les brevets associés à Wuan Xijiang. Vous retrouvez un dépôt reposant sur la 
technologie de Marinatech ; son identifiant constitue la réponse attendue.

🚩   2026 09154Flag : LH- -
NON NÉGOCIABLE
Question : Quelle est la référence de l'article de loi évoquant le refus de coopérer ?
Depuis le réseau du Lianhua, accédez au « Lianhua Legal Portal », qui regroupe les textes 
législatifs du pays.

Recherchez la « Loi sur le renseignement national de la République de Lianhua ». La 
disposition relative au refus de coopérer se trouve à l’article 9 du chapitre 3.
🚩 Flag : National Intelligence Act_chapter 3_Art. 9
MON PRÉCIEUX
Question : Quel « droit » évoque Zhou quand il parle de bénéficier de la valeur créée ? (Attention : 
flag en français.)
Depuis le site du Lianhua News Network, ouvrez l’onglet « Podcast ». À la fin de l’épisode gratuit « 
Why Strategic Materials Are the New Software », il est indiqué que les podcasts de LNN sont 
également disponibles sur les plateformes de streaming. Une recherche permet alors de

retrouver leur compte Spotify et l’épisode « From Research to National Capability ». En écoutant 
ou en transcrivant cet épisode, vous retrouvez les propos de Zhou Wenjie concernant 
Marinatech.
 Flag : droit inaliénable (ou indéniable ou incontestable selon les traducteurs ; les trois flags 🚩
étaient acceptés)
MESSAGE INTIME
Question : Par quelle phrase Wuan termine-t-il ce message adressé à un proche ?
Sachant qu’il est surveillé, Wuan dissimule un message destiné à son père dans une photo 
publiée sur son profil Qiao. 
 
Téléchargez l’image originale puis soumettez-la à un outil de stéganalyse tel qu’Aperi’Solve. 
L’outil effectue automatiquement plusieurs analyses de l’image : en consultant notamment les 
résultats Strings et zsteg, vous pouvez repérer du contenu qui n’appartient pas normalement à 
une simple photographie. L’analyse fait apparaître un message en clair ainsi que la présence 
d’un fichier ZIP dissimulé dans l’image, qu’il est alors possible d’extraire. La même analyse peut 
également être réalisée directement en ligne de commande avec zsteg.

L’archive ZIP est protégée par un mot de passe, mais le message découvert lors de l’analyse vous 
fournit un indice en faisant référence au vieux ferry de Haidong. Rendez-vous alors sur la page 
du wiki consacrée à Haidong : la photographie du ferry permet d’en retrouver le nom, dont la 
traduction, « lotus bleu », fournit le mot de passe permettant d’ouvrir l’archive.
Vous accédez ainsi au message caché par Wuan. Il ne vous reste plus qu’à en relever la dernière 
phrase pour obtenir la réponse attendue.
🚩 Flag : 最亲爱的妈妈
CAPITAL RISQUE 
Question : Indiquez l’adresse d’AquaVentis Partners.
Rendez-vous sur le site d’AquaVentis Partners puis consultez ses mentions légales. L’adresse 
officielle de l’entreprise y figure directement et fournit la réponse attendue.
🚩 Flag : Tour Eagle - 92060 La Défense
QUI A PIQUÉ MES PARTS 
Pour déterminer à quelle entité appartient AquaVentis, recherchez AquaVentis Partners sur le 
site Papiers.business, qui permet d’accéder aux informations légales de l’entreprise. Consultez 
ensuite ses statuts : la répartition du capital qui y figure fait apparaître qu’AquaVentis est 
détenue majoritairement par un fonds d’investissement luxembourgeois. Le nom de cet 
actionnaire majoritaire fournit la réponse attendue.

🚩 Flag : Blue Current Europe
OH LA BOULETTE 
Question : Quel détail justifie qu’Aquaventis ait pu agir de la sorte sans risquer un procès ?
Pour comprendre comment AquaVentis a pu céder ses participations dans Marinatech sans en 
informer préalablement les autres parties, retournez dans les statuts de l’entreprise. La réponse 
se trouve dans l’article 10, consacré à la transmission des actions, qui définit les conditions 
permettant cette cession.
Un article au contenu proche figurait également à l’article 4 de l’acte de cession, mais le format 
du flag, qui indiquait le nombre de chiffres attendu pour le numéro d’article, permettait de 
déterminer que ce n’était pas la réponse recherchée.
🚩 
Flag : Article 10 - Transmission des actions
POUPÉES RUSSES
Question : Quelle entreprise possède réellement Aquaventis Partners ?
Pour remonter jusqu’au véritable propriétaire d’AquaVentis Partners, poursuivez l’enquête sur 
son actionnaire majoritaire. En recherchant Blue Current Europe sur Papiers.business, vous 
découvrez que cette société luxembourgeoise est elle-même détenue à 100 % par Blue Current 
Holding Ltd, une entreprise enregistrée au Lianhua.

Ce nouveau pivot vous conduit sur l’intranet du Lianhua et sa base de données 
gouvernementale des entreprises. Recherchez-y Blue Current Holding Ltd afin de poursuivre 
la chaîne de détention et d’identifier l’entité qui se trouve réellement derrière AquaVentis 
Partners.
🚩 Flag : Hydronix Marine Corporation
COURRIER INDÉSIRABLE 2/2
Question : Qui se cache derrière ce mail ? Quel élément d'identification permet de confirmer 
l'identité de l'auteur ?
Analysez le mail de menace reçu par Enzo afin d’identifier le pixel de tracking. L’étude du domaine 
utilisé vous permet de découvrir un autre domaine lié grâce à sa règle SPF. Poursuivez l’analyse 
de ce nouveau domaine : sa règle DMARC fournit un pivot supplémentaire. Sur le dernier 
domaine, lotustrack.xyz, la règle RUF DMARC révèle une entrée DNS pointant vers pxltrakln.int.
Grâce au VPN, vous savez que l’extension .int correspond à une ressource liée au Lianhua. Le 
WHOIS local n’apporte d’abord rien de concluant. Reprenez alors l’adresse IP découverte dans « 
Courrier indésirable 1/2 » : 47.242.108.213, utilisée pour les sites du VLAN gouvernemental du 
Lianhua. Vous pouvez en déduire que pxltrakln.int possède probablement un équivalent 
en .gouv.ln.  L’analyse de ce domaine révèle un lien avec « Lianhua-Europe Cultural & Economic 
Cooperation Ltd. ». Une recherche de cette société dans la base gouvernementale des 
entreprises permet enfin d’identifier la personne qui se trouve derrière la structure et l’élément 
d’identification demandé.   Flag : Chen Rong_455 714 250 11562🚩



LE PACTE
Question : En cas d'impossibilité de transfert direct du capital en raison de clauses particulières, 
que doivent faire les parties ?
L’objectif est de retrouver le contrat entre AquaVentis et Hydronix. Commencez par identifier le 
site d’Hydronix depuis le registre des entreprises du Lianhua. Comme l’indique le wiki, un site 
local en .ln peut également disposer d’une version .int exposée sur Internet. Vous obtenez ainsi 
deux versions du site d’Hydronix :
• hydronix-marine-corporation.ln : version locale et à jour du site
• hydronix-marine-corporation.int : version internationale, non à jour
Comparez les pieds de page : la version .ln affiche v13.37 tandis que la version .int affiche v12.01. 
Le fichier robots.txt indique que le site fonctionne sous Apache. Sur la version locale à jour, une 
offre d’emploi montre par ailleurs qu’Hydronix recherche un ingénieur spécialisé dans la 
sécurisation des sites Internet.
Sur la version .int, une mauvaise configuration rend /server-status accessible. Le message « 
Misconfiguration detected: /s3cr3tfileS3cuR7s3d is accessible to everyone » révèle alors un 
répertoire exposé. Ouvrez-le pour retrouver le contrat entre AquaVentis et Hydronix.

La lecture du contrat vous permet enfin de retrouver la clause répondant à la question.
 Flag : The Parties shall examine an alternative structure providing substantially equivalent 🚩
economic or governance rights, subject at all times to applicable law.
