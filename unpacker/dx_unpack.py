import sys
from pydofus.dx import DX, InvalidDXFile

# python dx_unpack.py file.dx
# file output: file.swf

file = sys.argv[1]

dx_input = open(file, "rb")
swf_output = open(file.replace("dx", "swf"), "wb")

dx = DX(dx_input)
dx.read(swf_output)

dx_input.close()
swf_output.close()
