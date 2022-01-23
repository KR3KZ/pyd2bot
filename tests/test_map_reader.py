from time import perf_counter
from pyd2bot.gameData.mapReader import MapLoader


t = perf_counter()
map = MapLoader.load(193331716)
e = perf_counter() - t
print(f"took {e} seconds")
print(map.cells[3])

t = perf_counter()
MapLoader.load(193331716)
e = perf_counter() - t
print(f"took {e} seconds")
print(map.cells[3])