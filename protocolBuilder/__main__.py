#!/usr/bin/env python3
from pathlib import Path
import json 
import subprocess
import os
import com.ankamagames.dofus.Constants as Constants
from protocolBuilder.protocolParser2 import ProtocolParser
import protocolBuilder.exportClasses as exportClasses
work_dir = Path(os.path.dirname(__file__))
with open(work_dir / "config.json", 'r') as fp:
    settings = json.load(fp)
invoker_p = settings['dofusInvoker_path']
decoder_p = settings['ffdec_path']
def decompileSource(selectclass, src_dir):
    decompile_sources_cmd = f'"{decoder_p}" -config parallelSpeedUp=0 -selectclass {selectclass} -export script {src_dir} {invoker_p}'
    subprocess.call(decompile_sources_cmd, shell=True)
    
if __name__ == "__main__":
    
    
    
    # Decompile Dofus Invoker Sources
    selectclass = "com.ankamagames.dofus.BuildInfos,com.ankamagames.dofus.network.++,com.ankamagames.jerakine.network.++"
    src_dir = work_dir / "sources"
    decompileSource(selectclass, src_dir)

    # Parse protocol
    src_paths = [
        work_dir / "sources/scripts/com/ankamagames/dofus/network/types",
        work_dir / "sources/scripts/com/ankamagames/dofus/network/messages",
    ]
    
    protocol_json = ProtocolParser().run(src_paths)
    with open(Constants.PROTOCOL_SPEC_PATH, "w") as fp:
        json.dump(protocol_json, fp)

    # Export classes
    exportClasses.run()
        
    

    
    

