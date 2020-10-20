SRC_DIR = "C:\Users\khalid.majdoub\Documents"
if not SRC_DIR in sys.path: sys.path.append(SRC_DIR)
from farmapi import *
import frighost_fish as frifri


file_path = os.path.join(SRC_DIR, "dofus_bot.sikuli\\frighost_fish.sikuli\\path01.txt")
farmPath(file_path, frifri.PATTERNS)
    
