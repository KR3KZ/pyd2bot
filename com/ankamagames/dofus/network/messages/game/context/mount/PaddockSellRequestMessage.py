from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockSellRequestMessage(NetworkMessage):
    protocolId = 2370
    price:float
    forSale:bool
    
