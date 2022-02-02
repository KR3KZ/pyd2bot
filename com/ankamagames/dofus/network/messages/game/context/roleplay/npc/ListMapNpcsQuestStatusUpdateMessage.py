from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.npc.MapNpcQuestInfo import MapNpcQuestInfo


@dataclass
class ListMapNpcsQuestStatusUpdateMessage(NetworkMessage):
    mapInfo:list[MapNpcQuestInfo]
    
    
    def __post_init__(self):
        super().__init__()
    