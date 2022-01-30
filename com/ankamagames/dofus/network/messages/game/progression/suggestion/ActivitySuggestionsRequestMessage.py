from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ActivitySuggestionsRequestMessage(NetworkMessage):
    protocolId = 2540
    minLevel:int
    maxLevel:int
    areaId:int
    activityCategoryId:int
    nbCards:int
    
