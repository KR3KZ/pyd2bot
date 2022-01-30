from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseSearchMessage(NetworkMessage):
    protocolId = 6250
    genId:int
    follow:bool
    
