from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.web.haapi.BufferInformation import BufferInformation


@dataclass
class HaapiBufferListMessage(NetworkMessage):
    buffers:list[BufferInformation]
    
    
    def __post_init__(self):
        super().__init__()
    