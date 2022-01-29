
from abc import ABC, abstractproperty
from whistle import EventDispatcher


class IEventDispatcher(ABC):
    
    @abstractproperty
    def eventDispatcher() -> EventDispatcher:
        pass
