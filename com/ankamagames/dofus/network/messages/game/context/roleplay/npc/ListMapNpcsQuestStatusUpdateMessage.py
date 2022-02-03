from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.npc.MapNpcQuestInfo import MapNpcQuestInfo
    


class ListMapNpcsQuestStatusUpdateMessage(NetworkMessage):
    mapInfo:list['MapNpcQuestInfo']
    

    def init(self, mapInfo:list['MapNpcQuestInfo']):
        self.mapInfo = mapInfo
        
        super().__init__()
    
    