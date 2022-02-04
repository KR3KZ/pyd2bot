from whistle import EventDispatcher
from com.ankamagames.jerakine.metaclasses.singleton import Singleton



class BotEventsManager(metaclass=Singleton):

    def __init__(self):
        self._dipatcher = EventDispatcher()
        super().__init__()

    def add_listener(self, event_name, listener):
        self._dipatcher.add_listener(event_name, listener)
    
    def remove_listener(self, event_name, listener):
        self._dipatcher.remove_listener(event_name, listener)

    def has_listeners(self, event_name):
        return self._dipatcher.has_listeners(event_name)
    
    def dispatch(self, event_name, *args, **kwargs):
        self._dipatcher.dispatch(event_name, *args, **kwargs)
    
