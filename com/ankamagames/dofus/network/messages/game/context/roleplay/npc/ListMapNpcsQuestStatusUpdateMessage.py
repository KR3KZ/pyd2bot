from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.npc.MapNpcQuestInfo import MapNpcQuestInfo


class ListMapNpcsQuestStatusUpdateMessage(NetworkMessage):
    mapInfo:list[MapNpcQuestInfo]
    
    
