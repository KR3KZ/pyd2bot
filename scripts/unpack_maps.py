import os
from pathlib import Path
from tqdm import tqdm
import com.ankamagames.dofus.Constants as Constants
from dataAdapter.d2p import D2PReader

work_dir = Path(os.path.dirname(__file__))
D2P_MAPS_PATH = "C:\\Users\\majdoub\\AppData\\Local\\Ankama\\Dofus\\content\\maps"
out_dir = Constants.MAPS_PATH
    
def unpackD2pFile(file_p, out_dir):
    file_name = os.path.basename(file_p)
    print("D2P Unpacker for " + file_name)  
    with open(file_p, 'rb') as fp:
        d2p_reader = D2PReader(fp, False)
        d2p_reader.load()
        for name, specs in tqdm(d2p_reader.files.items()):
            mapid_mod_10, mapId = name.split("/")
            file_output_p = out_dir / mapid_mod_10 / mapId
            if not os.path.exists(file_output_p.parent):
                os.makedirs(file_output_p.parent)
            file_output = open(file_output_p, "wb")
            file_output.write(specs["binary"])
            file_output.close()

for d2p_file_path in Path(D2P_MAPS_PATH).glob("**/*.d2p"):
    unpackD2pFile(d2p_file_path, out_dir)