MAP_INFO_R = Region(5,858,306,168)

def changeMap(tgt):
    snippet = capture(MAP_INFO_R)
    while True:
        tgt.click()
        if waitVanish(Pattern(snippet).exact(), 20):
            break


regs = [Region(921,33,102,10), Region(1453,956,34,26)]
for r in regs:
    changeMap(r)