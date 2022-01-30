from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class InventoryWeightMessage(INetworkMessage):
    protocolId = 3751
    inventoryWeight:int
    shopWeight:int
    weightMax:int
    
    
