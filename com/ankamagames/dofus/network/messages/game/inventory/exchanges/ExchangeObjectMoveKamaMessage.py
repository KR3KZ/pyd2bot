from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeObjectMoveKamaMessage(INetworkMessage):
    protocolId = 427
    quantity:int
    
    
