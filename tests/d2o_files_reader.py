from time import perf_counter
from dataReader.d2o import D2OReader

f = r"C:\Users\majdoub\AppData\Local\Ankama\Dofus\data\common\AbuseReasons.d2o"

with open(f, "rb") as fp:
    r = D2OReader(fp).getObjects()
    l = len(r)
    for iobj in r:
        print(dir(iobj))
