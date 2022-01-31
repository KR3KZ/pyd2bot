from whistle import Event
from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class NetworkSentEvent(Event):
    
    EVENT_SENT:str = "messageSent"
    
    _message:INetworkMessage
    
    def __init__(self, msg:INetworkMessage):
        super().__init__()
        self._message = msg
    
    @property
    def message(self) -> INetworkMessage:
        return self._message
