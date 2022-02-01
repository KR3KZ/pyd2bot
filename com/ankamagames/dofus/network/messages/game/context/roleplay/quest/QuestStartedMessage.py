from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class QuestStartedMessage(INetworkMessage):
    protocolId = 475
    questId:int
    
    
