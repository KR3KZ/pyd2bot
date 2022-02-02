from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation


@dataclass
class HavenBagRoomUpdateMessage(NetworkMessage):
    action:int
    roomsPreview:list[HavenBagRoomPreviewInformation]
    
    
    def __post_init__(self):
        super().__init__()
    