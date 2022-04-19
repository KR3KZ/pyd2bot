from whistle import EventDispatcher
from com.ankamagames.jerakine.metaclasses.Singleton import Singleton



class BotEventsManager(metaclass=Singleton):
    SERVER_SELECTION = "server_selection"
    CHARACTER_SELECTION = "character_selection"
    SERVER_SELECTED = "server_selected"
    CHARACTER_SELECTED = "character_selected"
    SWITCH_TO_ROLEPLAY = "in_roleplay_context"
    SWITCH_TO_FIGHT = "in_flight_context"
    MAP_DATA_LOADED = "map_data_loaded"

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
    
