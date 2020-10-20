from sikuli.Sikuli import *


MAP_R = Region(0,28,1920,1002)
MAP_INFO_R = Region(17,73,77,29)


def loadFarmingPath(src_path):
    with open(src_path) as file:
        result=[]
        for line in file:
            resource_type, x, y, w, h = line.split(',')
            resource_region = Region(int(x), int(y), int(w), int(h))
            result.append((resource_region, resource_type))
    return result

def collectResource(resource_region, resource_type):
    match = resource_region.findBest(fish_patterns[resource_type])
    if match:
        current = Pattern(capture(resource_region))
        print("collecting '{}' at {}".format(resource_type, resource_region))
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
        
def farm(file_name):
    file_path = PATHS_DIR + "\\" + file_name
    path = loadFarmingPath(file_path)
    stats = {fish_t:0 for fish_t in fish_patterns}
    for rreg, rtype in path:
        if rtype == 'mapChange':
            changeMap(rreg)
        else:
            res = collectResource(rreg, rtype)
            if res :
                stats[rtype] += 1 
    return stats

