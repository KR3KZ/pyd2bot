from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ActivitySuggestionsMessage(INetworkMessage):
    protocolId = 5931
    lockedActivitiesIds:int
    unlockedActivitiesIds:int
    
    
