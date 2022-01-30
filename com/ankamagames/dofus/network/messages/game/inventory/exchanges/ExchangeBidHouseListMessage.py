from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseListMessage(INetworkMessage):
    protocolId = 2675
    id:int
    follow:bool
    
    
