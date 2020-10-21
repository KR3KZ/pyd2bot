import re

reg_patt = "map\s*\[\s*(-*\d+)\s*,\s*(-*\d+)\s*\]"


str_test = "map[-10,20]"

sx, sy = re.findall(reg_patt, str_test)[0]

print(int(sx), int(sy))

