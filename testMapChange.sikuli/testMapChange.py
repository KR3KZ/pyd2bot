tr = Region(16,867,305,162)

class Observer(threading.Thread):
    def __init__(self, region, pattern, scanRate = 3):
        threading.Thread.__init__(self)
        self.pattern       = pattern
        self.scanRate      = scanRate   
        self.region = region
    def run(self):
        while(not exitSignal.is_set()):
            try:
                match = self.region.wait(self.pattern, 1./self.scanRate)         
                break
            except:
                pass

with tr:
    onChange(100)
    observe(12)
    stopObserver()

with tr:
    onChange(100)
    observe(12)
    stopObserver()