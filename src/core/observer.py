import threading


class Observer(threading.Thread):
    class Mode:
        APPEAR = 1
        VANISH = 2
        CHANGE = 3

    def __init__(self, region, pattern, callback=None, mode=Mode.APPEAR):
        threading.Thread.__init__(self)
        self.region = region
        self.callback = callback
        self.stopSignal = threading.Event()
        self.changed = threading.Event()
        self.pattern = pattern
        self.mode = mode

    def stop(self):
        self.region.stopWait.set()

    def run(self):
        if self.mode == self.Mode.APPEAR:
            self.region.waitAppear(self.pattern)
        elif self.mode == self.Mode.VANISH:
            self.region.waitVanish(self.pattern)
        elif self.mode == self.Mode.CHANGE:
            self.region.waitChange()
            self.changed.set()
        if self.callback:
            self.callback()