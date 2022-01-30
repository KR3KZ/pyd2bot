from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestStartedMessage(INetworkMessage):
    protocolId = 475
    questId:int
    
    
