from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class RefreshFollowedQuestsOrderRequestMessage(INetworkMessage):
    protocolId = 1088
    quests:int
    
    
