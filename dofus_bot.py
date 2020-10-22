SRC_DIR = "C:\Users\khalid.majdoub\Documents"
if not SRC_DIR in sys.path: sys.path.append(SRC_DIR)
import frighost_fish as frifri


MAP_R = Region(0,28,1920,1002)
MAP_INFO_R = tr = Region(13,865,307,169)


def waitForChange(region):
    with region:
        onChange(100)
        observe(10)
        stopObserver()


def loadFarmingPath(src_path):
    with open(src_path) as file:
        result = []
        for line in file:
            if line:
                if line.startswith("#"):
                    continue
                data_list = line.split(',')
                print(data_list)
                if len(data_list) < 5:
                    continue
                rtype = data_list[0]  
                rec = [int(e.strip('\n')) for e in data_list[1:]]
                resource_region = Region(*rec)
                result.append((resource_region, rtype))
    return result


def collectResource(resource_region, resource_patterns):
    match = resource_region.findBest(resource_patterns)
    if match:
        resource_region.hover()
        sleep(0.3)
        current = Pattern(capture(resource_region))
        resource_region.click()
        with resource_region:
            waitForChange(resource_region)
            waitVanish(current.similar(0.6))
        return True
    return False


def changeMap(tgt):
    print("changing map")
    cp = capture(MAP_INFO_R)
    tgt.click()
    while MAP_INFO_R.exists(Pattern(cp).similar(0.85)):
        wait(0.5)
        

def farmPath(file_path, resource_patterns):
    path = loadFarmingPath(file_path)
    for rreg, rtype in path:
        if rtype == 'mapChange':
            changeMap(rreg)
        else:
            collectResource(rreg, resource_patterns[rtype])
    return stats

file_path = os.path.join(SRC_DIR, "dofus_bot.sikuli\\frighost_fish.sikuli\\path01.txt")
farmPath(file_path, frifri.PATTERNS)
    


