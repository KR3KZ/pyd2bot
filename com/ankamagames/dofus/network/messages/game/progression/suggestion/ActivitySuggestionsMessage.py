from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ActivitySuggestionsMessage(NetworkMessage):
    protocolId = 5931
    lockedActivitiesIds:int
    unlockedActivitiesIds:int
    
    
