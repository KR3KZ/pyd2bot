from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.havenbag.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
    


class HavenBagRoomUpdateMessage(NetworkMessage):
    action:int
    roomsPreview:list['HavenBagRoomPreviewInformation']
    

    def init(self, action:int, roomsPreview:list['HavenBagRoomPreviewInformation']):
        self.action = action
        self.roomsPreview = roomsPreview
        
        super().__init__()
    
    