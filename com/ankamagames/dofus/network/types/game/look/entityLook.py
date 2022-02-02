from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.look.SubEntity import SubEntity


@dataclass
class EntityLook(NetworkMessage):
    bonesId:int
    skins:list[int]
    indexedColors:list[int]
    scales:list[int]
    subentities:list[SubEntity]
    
    
    def __post_init__(self):
        super().__init__()
    