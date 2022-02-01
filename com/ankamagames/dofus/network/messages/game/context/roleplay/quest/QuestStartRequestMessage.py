from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestStartRequestMessage(INetworkMessage):
    protocolId = 6071
    questId:int
    
    
