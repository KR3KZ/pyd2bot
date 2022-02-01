from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseListMessage(INetworkMessage):
    protocolId = 2675
    id:int
    follow:bool
    
    
