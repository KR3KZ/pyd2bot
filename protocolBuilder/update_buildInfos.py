#!/usr/bin/env python3
from pathlib import Path
import json 
import subprocess
import os
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
    selectclass = "com.ankamagames.dofus.BuildInfos"
    src_dir = work_dir / "sources"
    decompileSource(selectclass, src_dir)
