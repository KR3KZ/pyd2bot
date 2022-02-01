from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestStepInfoRequestMessage(INetworkMessage):
    protocolId = 5562
    questId:int
    
    
