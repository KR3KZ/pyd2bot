from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ActivitySuggestionsMessage(NetworkMessage):
    lockedActivitiesIds:list[int]
    unlockedActivitiesIds:list[int]
    
    
