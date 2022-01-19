import sys, json
from pydofus.d2i import D2I, InvalidD2IFile

# python d2i_unpack.py file.d2i
# file output: file.json

file = sys.argv[1]

d2i_input = open(file, "rb")
json_output = open(file.replace("d2i", "json"), "w", encoding="utf-8")

d2i = D2I(d2i_input)
data = d2i.read()

json.dump(data, json_output, indent=2, ensure_ascii=False)

d2i_input.close()
json_output.close()
