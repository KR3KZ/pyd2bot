from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.web.haapi.BufferInformation import BufferInformation
    


class HaapiBufferListMessage(NetworkMessage):
    buffers:list['BufferInformation']
    

    def init(self, buffers:list['BufferInformation']):
        self.buffers = buffers
        
        super().__init__()
    
    