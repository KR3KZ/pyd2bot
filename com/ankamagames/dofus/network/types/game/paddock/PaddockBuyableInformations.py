from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockBuyableInformations(NetworkMessage):
    protocolId = 3536
    price:float
    locked:bool
    
