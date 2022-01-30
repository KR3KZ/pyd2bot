from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.npc.MapNpcQuestInfo import MapNpcQuestInfo


class ListMapNpcsQuestStatusUpdateMessage(NetworkMessage):
    protocolId = 5996
    mapInfo:MapNpcQuestInfo
    
