from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ActivitySuggestionsMessage(INetworkMessage):
    protocolId = 5931
    lockedActivitiesIds:int
    unlockedActivitiesIds:int
    
    
