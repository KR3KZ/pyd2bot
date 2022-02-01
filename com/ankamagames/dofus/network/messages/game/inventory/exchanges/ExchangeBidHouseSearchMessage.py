from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseSearchMessage(INetworkMessage):
    protocolId = 6250
    genId:int
    follow:bool
    
    
