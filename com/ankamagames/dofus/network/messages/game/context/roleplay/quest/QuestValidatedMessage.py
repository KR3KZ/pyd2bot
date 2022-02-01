from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestValidatedMessage(INetworkMessage):
    protocolId = 1984
    questId:int
    
    
