# bot2pix

## Intro
Ce projet a pour objectif de developper un bot pixel pour dofus 2, qui utilise un sniffer pour compléter certaines infos difficiles à parser visuellement.
Pour la partie visuelle, il se base sur cv2 de openCV, et pour la partie sniffing il se base sur scapy et wincap.
Le sniffer decode les messages à partir d'un fichier json ("protocol.json") qui contient les données sur les packets du protocol dofus 2.
Ce fichier est construit à partir des sources de dofus 2 (DofusInvoker.swf), cette partie a été construite à Partir du fameux LaBot de Louis Abraham.
Le bot pour le moment ne tourne que pour la résolution 1920 x 1080.

# Dependences 
## dependences python
Commencer d'abord par installer les dependeces python avec `pip install -r requirements.txt".

## decodeur flash
Après, il faudra telecharger et installer le decodeur flash ffdec de l'url, qui va permettre de decompiler une partie des sources de dofus [JPEXS
FFDec](https://github.com/jindrapetrik/jpexs-decompiler).


# Mode Emploi 
Après installation des dépendences il faudra suivre les étapes suivantes pour pouvoir lancer une instance le bot correctement et s'amuser avec :).
## Build du protocol 
Lancer la commande `python -m src.network.protocol_builder`.

Maintenant tout est prêt, vous pouvez alors vous rendre dans le dossier examples et voir comment instancier un python-bot et le lancer.


