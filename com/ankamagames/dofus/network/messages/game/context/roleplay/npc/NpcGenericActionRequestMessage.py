from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class NpcGenericActionRequestMessage(NetworkMessage):
    npcId:int
    npcActionId:int
    npcMapId:int
    
    
    def __post_init__(self):
        super().__init__()
    