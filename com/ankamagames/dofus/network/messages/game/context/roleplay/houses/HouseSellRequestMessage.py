from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseSellRequestMessage(NetworkMessage):
    instanceId:int
    amount:int
    forSale:bool
    
    
