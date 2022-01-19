import sys, json
from pydofus.ele import ELE, InvalidELEFile

# python ele_unpack.py file.ele
# file output: file.json

file = sys.argv[1]

ele_input = open(file, "rb")
json_output = open(file.replace(".ele", ".json"), "w")

ele = ELE(ele_input)
data = ele.read()

json.dump(data, json_output, indent=2)

ele_input.close()
json_output.close()
