from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestValidatedMessage(INetworkMessage):
    protocolId = 1984
    questId:int
    
    
