# SIGNATURE_KEY_DATA = Constants_SIGNATURE_KEY_DATA

import os
from pathlib import Path


LOG_UPLOAD_MODE = False

EVENT_MODE = False

EVENT_MODE_PARAM = ""

CHARACTER_CREATION_ALLOWED = True

PRE_GAME_MODULE = ["Ankama_Connection"]

COMMON_GAME_MODULE = ["Ankama_Common","Ankama_Config","Ankama_Tooltips","Ankama_Console","Ankama_ContextMenu"]

ADMIN_MODULE = ["Ankama_Admin"]

DETERMINIST_TACKLE = True

DATASTORE_MODULE_DEBUG = False

MAX_LOGIN_ATTEMPTS = 3

ROOTDIR = Path(os.path.dirname(__file__))
MAPS_PATH = ROOTDIR / "gameData/dlmMaps"
PROTOCOL_SPEC_PATH = ROOTDIR / "network/protocol_spec.json"