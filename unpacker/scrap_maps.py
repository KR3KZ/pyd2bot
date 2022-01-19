from pathlib import Path
from pydofus.dlm import DLM, InvalidDLMFile
import os 
import json

workdir = Path(__file__).parent
mapsdir = workdir / "output"
scrapeddir = workdir / "scraped_ouputs"

if not os.path.exists(scrapeddir):
    os.makedirs(scrapeddir)
    
for dlm_file_path in mapsdir.glob("**/*.dlm"):
    dst_f = scrapeddir / dlm_file_path.name.replace("dlm", "json")
    with open(dlm_file_path, "rb") as dlm_input:
        dlm = DLM(dlm_input, "649ae451ca33ec53bbcbcc33becf15f4")
        data = dlm.read()
    with open(dst_f, "w") as fp:
        json.dump(data, fp, indent=2)