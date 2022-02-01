from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivitySuggestionsRequestMessage(NetworkMessage):
    minLevel:int
    maxLevel:int
    areaId:int
    activityCategoryId:int
    nbCards:int
    
    
