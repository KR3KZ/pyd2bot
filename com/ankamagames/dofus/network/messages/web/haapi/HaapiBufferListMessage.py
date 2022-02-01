from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.web.haapi.BufferInformation import BufferInformation


class HaapiBufferListMessage(NetworkMessage):
    buffers:list[BufferInformation]
    
    
