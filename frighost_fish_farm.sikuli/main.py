WORK_DIR = "C:\Users\khalid.majdoub\Documents\\botpix0.sikuli"
PATHS_DIR = WORK_DIR + "\\paths"
if not src_dir in sys.path: sys.path.append(working_dir)
from farm_api import *

MAP_R = Region(0,28,1920,1002)
MAP_INFO_R = Region(17,73,77,29)

fish_patterns = {
    "kralamoure": [Pattern("paths\frighost001\patterns\kralamoure001.png").similar(0.41), Pattern("kralamoure002.png").similar(0.52), Pattern("kralamoure003.png").similar(0.61)],
    "poissonPane": [Pattern("poissonPane001.png").similar(0.57)],
    "poisskaille": [Pattern("poisskaille001.png").similar(0.51)],
    "sardineBrillante": [Pattern("1603163659240.png").similar(0.51),Pattern("1603164702180.png").similar(0.56)]
}

farmFish("frighost.txt")

Region(Region(149,463,89,65))
