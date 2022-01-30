from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity


class ObjectsQuantityMessage(NetworkMessage):
    protocolId = 5570
    objectsUIDAndQty:ObjectItemQuantity
    
    
