from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class QuestStepInfoRequestMessage(INetworkMessage):
    protocolId = 5562
    questId:int
    
    
