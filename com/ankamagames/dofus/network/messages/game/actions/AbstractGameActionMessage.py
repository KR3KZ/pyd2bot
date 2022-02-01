from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AbstractGameActionMessage(INetworkMessage):
    protocolId = 5037
    actionId:int
    sourceId:int
    
    
