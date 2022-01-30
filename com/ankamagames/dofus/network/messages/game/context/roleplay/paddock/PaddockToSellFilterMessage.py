from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PaddockToSellFilterMessage(INetworkMessage):
    protocolId = 8388
    areaId:int
    atLeastNbMount:int
    atLeastNbMachine:int
    maxPrice:int
    orderBy:int
    
    
