from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation


class HavenBagRoomUpdateMessage(NetworkMessage):
    protocolId = 1606
    action:int
    roomsPreview:HavenBagRoomPreviewInformation
    
