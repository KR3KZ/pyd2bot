from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantity import ObjectItemQuantity


class ObjectsQuantityMessage(INetworkMessage):
    protocolId = 5570
    objectsUIDAndQty:ObjectItemQuantity
    
    
