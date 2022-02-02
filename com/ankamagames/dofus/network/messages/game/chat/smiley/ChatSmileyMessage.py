from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ChatSmileyMessage(NetworkMessage):
    entityId:int
    smileyId:int
    accountId:int
    
    
    def __post_init__(self):
        super().__init__()
    