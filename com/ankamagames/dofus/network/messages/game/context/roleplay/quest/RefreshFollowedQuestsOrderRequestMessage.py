from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RefreshFollowedQuestsOrderRequestMessage(NetworkMessage):
    quests:list[int]
    
    
