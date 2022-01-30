from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseSellRequestMessage(NetworkMessage):
    protocolId = 9330
    instanceId:int
    amount:float
    forSale:bool
    
