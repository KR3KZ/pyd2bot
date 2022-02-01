from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeObjectMoveMessage(INetworkMessage):
    protocolId = 5229
    objectUID:int
    quantity:int
    
    
