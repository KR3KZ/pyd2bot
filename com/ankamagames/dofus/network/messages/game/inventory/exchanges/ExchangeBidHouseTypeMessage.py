from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseTypeMessage(NetworkMessage):
    protocolId = 4445
    type:int
    follow:bool
    
    
