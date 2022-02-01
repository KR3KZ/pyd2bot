from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockSellRequestMessage(INetworkMessage):
    protocolId = 2370
    price:int
    forSale:bool
    
    
