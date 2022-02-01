from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation


class HavenBagRoomUpdateMessage(NetworkMessage):
    action:int
    roomsPreview:list[HavenBagRoomPreviewInformation]
    
    
