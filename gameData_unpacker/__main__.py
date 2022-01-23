import io, sys, os, json
from pathlib import Path
from tqdm import tqdm
from .d2p import D2PReader, InvalidD2PFile
from .swl import SWLReader, InvalidSWLFile


work_dir = Path(os.path.dirname(__file__))
D2P_MAPS_PATH = "C:\\Users\\majdoub\\AppData\\Local\\Ankama\\Dofus\\content\\maps\\maps0.d2p"
out_dir = work_dir / "../pyd2bot/gameData/dlm_maps"

def unpackD2pFile(file_p, out_dir):
    file_name = os.path.basename(file_p)
    print("D2P Unpacker for " + file_name)  
    with open(file_p, 'rb') as fp:
        file_stream = fp
        d2p_reader = D2PReader(file_stream, False)
        d2p_reader.load()
        for name, specs in tqdm(d2p_reader.files.items()):
            mapid_mod_10, filename = name.split("/")
            file_output_p = out_dir / mapid_mod_10 / filename
            if not os.path.exists(file_output_p.parent):
                os.makedirs(file_output_p.parent)
            file_output = open(file_output_p, "wb")
            file_output.write(specs["binary"])
            file_output.close()

unpackD2pFile(D2P_MAPS_PATH, out_dir)