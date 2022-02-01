from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeObjectUseInWorkshopMessage(INetworkMessage):
    protocolId = 5412
    objectUID:int
    quantity:int
    
    
