from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ActivitySuggestionsRequestMessage(INetworkMessage):
    protocolId = 2540
    minLevel:int
    maxLevel:int
    areaId:int
    activityCategoryId:int
    nbCards:int
    
    
