from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeOkMultiCraftMessage(INetworkMessage):
    protocolId = 2595
    initiatorId:int
    otherId:int
    role:int
    
    
