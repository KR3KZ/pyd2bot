from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation


class HavenBagRoomUpdateMessage(INetworkMessage):
    protocolId = 1606
    action:int
    roomsPreview:HavenBagRoomPreviewInformation
    
    