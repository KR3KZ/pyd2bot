from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class MimicryObjectPreviewMessage(NetworkMessage):
    protocolId = 1198
    result:ObjectItem
    
    
