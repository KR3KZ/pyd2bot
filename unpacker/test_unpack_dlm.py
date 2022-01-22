from pydofus.dlm import DLM, Map


file = r"C:\Users\majdoub\OneDrive\Documents\pyd2bot\unpacker\output\maps1_4.d2p\3\75497473.dlm"

dlm_input = open(file, "rb").read()

dlm = DLM("649ae451ca33ec53bbcbcc33becf15f4")

map = dlm.read(dlm_input)

print(map.leftNeighbourId)
print(map.rightNeighbourId)
print(map.topNeighbourId)
print(map.bottomNeighbourId)