import sys, json
from pydofus.dlm import DLM, InvalidDLMFile

# python dlm_pack.py file.json
# file output: file.dlm

file = sys.argv[1]

json_input = open(file, "r")
dlm_output = open(file.replace("json", "dlm"), "wb")

dlm = DLM(dlm_output, "649ae451ca33ec53bbcbcc33becf15f4")
data = dlm.write(json.load(json_input))

json_input.close()
dlm_output.close()
