from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockBuyableInformations(INetworkMessage):
    protocolId = 3536
    price:int
    locked:bool
    
    
