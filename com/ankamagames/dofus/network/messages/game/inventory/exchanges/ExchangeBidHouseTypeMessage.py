from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseTypeMessage(INetworkMessage):
    protocolId = 4445
    type:int
    follow:bool
    
    
