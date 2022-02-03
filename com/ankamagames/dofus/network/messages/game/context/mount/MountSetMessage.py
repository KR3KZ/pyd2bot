from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
    


class MountSetMessage(NetworkMessage):
    mountData:'MountClientData'
    

    def init(self, mountData:'MountClientData'):
        self.mountData = mountData
        
        super().__init__()
    
    