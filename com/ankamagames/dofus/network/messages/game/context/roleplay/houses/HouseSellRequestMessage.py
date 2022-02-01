from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseSellRequestMessage(INetworkMessage):
    protocolId = 9330
    instanceId:int
    amount:int
    forSale:bool
    
    
