from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class AccessoryPreviewMessage(NetworkMessage):
    look:EntityLook
    
    
    def __post_init__(self):
        super().__init__()
    