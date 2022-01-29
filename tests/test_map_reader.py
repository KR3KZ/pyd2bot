import pickle
from time import perf_counter
from com.ankamagames.jerakine.resources.loaders.MapLoader import MapLoader

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
    mapid = 193331716    
    mapx = MapLoader.load(mapid)
    with open(r"tests\193331716.pkl", "rb") as f:
        mapy = pickle.load(f)
    assert mapx.id == mapy.id
    assert mapx.cells == mapy.cells

if __name__ == '__main__':
    test_load_map()
    test_cach()
        

