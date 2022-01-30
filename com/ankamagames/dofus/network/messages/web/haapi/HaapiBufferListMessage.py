from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.web.haapi.BufferInformation import BufferInformation


class HaapiBufferListMessage(NetworkMessage):
    protocolId = 518
    buffers:list[BufferInformation]
    
