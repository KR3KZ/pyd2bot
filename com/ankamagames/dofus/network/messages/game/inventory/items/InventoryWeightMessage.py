from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class InventoryWeightMessage(INetworkMessage):
    protocolId = 3751
    inventoryWeight:int
    shopWeight:int
    weightMax:int
    
    
