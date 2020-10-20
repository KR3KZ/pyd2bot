from sikuli.Sikuli import *


MAP_R = Region(0,28,1920,1002)
MAP_INFO_R = Region(17,73,77,29)


def loadFarmingPath(src_path):
    with open(src_path) as file:
        result=[]
        for line in file:
            if line.startswith("#"):
                continue
            resource_type, x, y, w, h = line.split(',')
            resource_region = Region(int(x), int(y), int(w), int(h))
            result.append((resource_region, resource_type))
    return result

def collectResource(resource_region, resource_patterns):
    match = resource_region.findBest(resource_patterns)
    if match:
        current = Pattern(capture(resource_region))
        resource_region.click()
        with resource_region:
            onChange(100)           
            observe(10)   
            stopObserver()
            waitVanish(current.similar(0.6))
        return True
    return False
        
def changeMap(tgt):
    print("changing map")
    mP = Pattern(capture(MAP_INFO_R))
    while(True):
        tgt.click()
        if MAP_INFO_R.waitVanish(mP.exact(), 5):
            sleep(1)
            break      
        
def farmPath(file_path, resource_patterns):
    path = loadFarmingPath(file_path)
    for rreg, rtype in path:
        if rtype == 'mapChange':
            changeMap(rreg)
        else:
            collectResource(rreg, resource_patterns[rtype])
    return stats





