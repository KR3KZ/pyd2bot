from time import perf_counter
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.data.I18nFileAccessor import I18nFileAccessor

t = perf_counter()
I18nFileAccessor().init(r"C:\Users\majdoub\AppData\Local\Ankama\Dofus\data\i18n\i18n_fr.d2i")
print("Init:", perf_counter() - t)

t = perf_counter()
r = I18n.getText(752599)
print("read:", perf_counter() - t)
assert r == "Cimetière d'Astrub"
t = perf_counter()
r = I18n.getText(752598)
print("read:", perf_counter() - t)
print(r)


