from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class RefreshFollowedQuestsOrderRequestMessage(INetworkMessage):
    protocolId = 1088
    quests:int
    
    
