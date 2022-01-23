import sys, json
from pydofus.dlm import DLM, InvalidDLMFile

# python dlm_unpack.py file.dlm
# file output: file.json

file = sys.argv[1]

dlm_input = open(file, "rb")
json_output = open(file.replace("dlm", "json"), "w")

dlm = DLM(dlm_input, "649ae451ca33ec53bbcbcc33becf15f4")
data = dlm.read()

json.dump(data, json_output, indent=2)

dlm_input.close()
json_output.close()
