from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class InventoryWeightMessage(NetworkMessage):
    protocolId = 3751
    inventoryWeight:int
    shopWeight:int
    weightMax:int
    
