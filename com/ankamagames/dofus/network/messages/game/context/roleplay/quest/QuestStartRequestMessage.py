from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestStartRequestMessage(INetworkMessage):
    protocolId = 6071
    questId:int
    
    
