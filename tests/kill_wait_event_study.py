import threading
from time import perf_counter
import time

def or_set(self):
    self._set()
    self.changed()

def or_clear(self):
    self._clear()
    self.changed()

def orify(e, changed_callback):
    e._set = e.set
    e._clear = e.clear
    e.changed = changed_callback
    e.set = lambda: or_set(e)
    e.clear = lambda: or_clear(e)

def OrEvent(*events):
    or_event = threading.Event()
    def changed():
        bools = [e.is_set() for e in events]
        if any(bools):
            or_event.set()
        else:
            or_event.clear()
    for e in events:
        orify(e, changed)
    changed()
    return or_event

def wait_on(name, e, t):
    st = perf_counter()
    e.wait(t)
    print("waited on {} for {}s".format(name, perf_counter() - st))

def set_after(name, e, t):
    time.sleep(t)
    e.set()
    
def test():
    import time
    e1 = threading.Event()
    e2 = threading.Event()
    or_e = OrEvent(e1, e2)
    # threading.Thread(target=wait_on, args=('or_e', or_e, 20)).start()
    threading.Thread(target=set_after, args=('or_e', e1, 5)).start()

    st = perf_counter()
    or_e.wait()
    print("waited for {}s".format(perf_counter() - st))

    
if __name__=='__main__':
    test()

