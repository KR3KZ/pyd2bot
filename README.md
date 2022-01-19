# pyd2bot

## Intro
Ce projet a pour objectif de developper un bot fullsocket pour dofus 2 100% en python.

## Setup des sources dans site-packages de python
Vous devez executer le script shell setup.sh affin que le chemin des sources soit connu par python
`./setup.py`

# Dependences 
## dependences python
Commencer d'abord par installer les dependeces python avec `pip install -r requirements.txt".
## decodeur flash
Après, il faudra telecharger et installer le decodeur flash ffdec de l'url, qui va permettre de decompiler une partie des sources de dofus [JPEXS
FFDec](https://github.com/jindrapetrik/jpexs-decompiler).
# Build 
Après installation des dépendences il faudra suivre les étapes suivantes pour pouvoir lancer une instance le bot correctement et s'amuser avec :).
## Build du protocol 
Commencer par modifier le fichier se trouvant dans "protocol_builder/config.json", vous devez y renseigner deux choses:
- "dofusInvoker_path" (chemin vers le fichier dofusInvoker): example "C:\\Users\\<ton_user_name>\\AppData\\Local\\Ankama\\Dofus\\DofusInvoker.swf",
- "ffdec_path" (chemin vers l'executable du decodeur flash): "C:\\Program Files (x86)\\FFDec\\ffdec.bat"

Lancer Après la commande `python -m protocol_builder`.
## Extraction des données de jeux (sur les maps, la pub_key du client ...)
Section pas encore rédigée
# Lancement d'une instance de bot
Rendez-vous dans le dossier tests pour trouver des examples de lancement de bots.
