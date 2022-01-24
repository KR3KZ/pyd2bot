from time import perf_counter
from pyd2bot.gameData.mapReader import MapLoader


def test_cach():
    t = perf_counter()
    map1 = MapLoader.load(193331716)
    e1 = perf_counter() - t
    print(f"took {e1} seconds")

    t = perf_counter()
    map2 = MapLoader.load(193331716)
    e2 = perf_counter() - t
    print(f"took {e2} seconds")
    
    assert map1 == map2
    assert e2 < e1

def test_load_map():
    import json 
    with open("./tests/193331717.json") as f:
        data = json.load(f)
    grid = MapLoader.load(193331717)
    for i, cell in enumerate(data["cells"]):
        for key in cell:
            if cell[key] != grid.cells[i].__dict__[key]:
                print("key: {0}, value: {1} but old read value {2}".format(key, grid.cells[i].__dict__[key], cell[key]))
                
test_load_map()
test_cach()
    

