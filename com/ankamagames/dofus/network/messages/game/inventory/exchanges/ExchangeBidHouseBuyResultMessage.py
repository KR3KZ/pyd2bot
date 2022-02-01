from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHouseBuyResultMessage(INetworkMessage):
    protocolId = 3743
    uid:int
    bought:bool
    
    
