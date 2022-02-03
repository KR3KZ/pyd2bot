import pyamf

file = r"C:\Users\majdoub\AppData\Roaming\Dofus\Jerakine_classAlias.dat"

with open(file, "rb") as fp:
    data = fp.read()
    c = pyamf.decode(data)
    obj = next(c)
    print(obj["classAliasList"])
    print("--------------")