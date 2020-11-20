import threading


class Observer(threading.Thread):
    class Mode:
        APPEAR = 1
        VANISH = 2
        CHANGE = 3

    def __init__(self, region, pattern=None, callback=None, mode=Mode.APPEAR, rate=0):
        threading.Thread.__init__(self)
        self.region = region
        self.callback = callback
        self.stopSignal = threading.Event()
        self.changed = threading.Event()
        self.vanished = threading.Event()
        self.mode = mode
        self.rate = rate
        if self.mode == self.Mode.CHANGE:
            self.pattern = self.region.capture().copy()
        else:
            self.pattern = pattern

    def stop(self):
        self.stopSignal.set()
        self.region.stopWait.set()

    def run(self):
        self.stopSignal.clear()
        while not self.stopSignal.is_set():
            if self.mode == self.Mode.APPEAR:
                self.region.waitAppear(self.pattern, rate=self.rate)
            elif self.mode == self.Mode.VANISH:
                self.region.waitVanish(self.pattern)
                self.vanished.set()
            elif self.mode == self.Mode.CHANGE:
                self.region.waitVanish(self.pattern)
                self.changed.set()
            if not self.stopSignal.is_set() and self.callback:
                self.callback()


if __name__ == "__main__":
    from core.region import Region
    from core import dofus
    from core import env

    # env.focusDofusWindow()
    # dofus.PA_R.highlight(1)
    pa_observer = Observer(dofus.PA_R, mode=Observer.Mode.CHANGE)
    pa_observer.start()
    if pa_observer.changed.wait(10):
        print("changed")
