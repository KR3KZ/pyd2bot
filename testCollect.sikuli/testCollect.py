def collectResource(region):
    p0 = Pattern(capture(region))
    sleep(0.2)
    region.hover()
    sleep(0.2)
    p1 = Pattern(capture(region))
    if not region.exists(p0):
        print("no")
        region.click()
        sleep(0.5)
        while region.exists(p1.exact(), 1):
            wait(0.1)
rgs = [Region(1036,761,68,43), Region(904,825,69,50), Region(470,564,76,51), Region(434,372,56,41), Region(509,318,79,59)]
for r in rgs:
    collectResource(r)