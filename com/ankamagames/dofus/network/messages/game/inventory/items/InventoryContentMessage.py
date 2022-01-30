from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class InventoryContentMessage(NetworkMessage):
    protocolId = 4197
    objects:list[ObjectItem]
    kamas:float
    
