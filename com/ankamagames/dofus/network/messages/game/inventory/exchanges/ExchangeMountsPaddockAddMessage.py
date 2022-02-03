from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.mount.MountClientData import MountClientData
    


class ExchangeMountsPaddockAddMessage(NetworkMessage):
    mountDescription:list['MountClientData']
    

    def init(self, mountDescription:list['MountClientData']):
        self.mountDescription = mountDescription
        
        super().__init__()
    
    