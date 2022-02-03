from ctypes import oledll
import pyamf
import miniamf

file = r"C:\Users\majdoub\AppData\Roaming\Dofus\Dofus_ComputerOptions.dat"

with open(file, "rb") as fp:
    data = fp.read()
    c = pyamf.decode(data)
    r = miniamf.decode(data)
    print(len(list(c)))