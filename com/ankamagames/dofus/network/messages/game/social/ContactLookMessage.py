from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class ContactLookMessage(NetworkMessage):
    requestId:int
    playerName:str
    playerId:int
    look:EntityLook
    
    
    def __post_init__(self):
        super().__init__()
    