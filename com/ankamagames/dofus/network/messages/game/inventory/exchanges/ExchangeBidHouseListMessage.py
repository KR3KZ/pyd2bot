from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseListMessage(NetworkMessage):
    protocolId = 2675
    id:int
    follow:bool
    
    
