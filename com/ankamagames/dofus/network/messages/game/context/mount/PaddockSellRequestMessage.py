from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockSellRequestMessage(INetworkMessage):
    protocolId = 2370
    price:int
    forSale:bool
    
    
