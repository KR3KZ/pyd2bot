#!/usr/bin/env python3
from pathlib import Path
from .protocol_parser import ProtocolParser
import json 
import subprocess
import os

work_dir = Path(os.path.dirname(__file__))

if __name__ == "__main__":
    
    with open(work_dir / "config.json", 'r') as fp:
        settings = json.load(fp)
    
    # Decompile Dofus Invoker Sources
    selectclass = "com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++"
    invoker_p = settings['dofusInvoker_path']
    decoder_p = settings['ffdec_path']
    src_dir = work_dir / "sources"
    decompile_sources_cmd = f'"{decoder_p}" -config parallelSpeedUp=0 -selectclass {selectclass} -export script {src_dir} {invoker_p}'
    subprocess.call(decompile_sources_cmd, shell=True)

    # Parse protocol
    src_paths = [
        work_dir / "sources/scripts/com/ankamagames/dofus/network/types",
        work_dir / "sources/scripts/com/ankamagames/dofus/network/messages",
    ]
    
    protocol_json = ProtocolParser.run(src_paths)
    with (work_dir / "../pyd2bot/network/protocol_spec.json").open("w") as fp:
        json.dump(protocol_json, fp)
        
    

    
    

