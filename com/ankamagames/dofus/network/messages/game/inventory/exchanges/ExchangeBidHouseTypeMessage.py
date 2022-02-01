from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseTypeMessage(INetworkMessage):
    protocolId = 4445
    type:int
    follow:bool
    
    
