from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHouseSearchMessage(INetworkMessage):
    protocolId = 6250
    genId:int
    follow:bool
    
    
