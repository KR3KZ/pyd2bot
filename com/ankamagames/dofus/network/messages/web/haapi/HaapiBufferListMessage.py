from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.web.haapi.BufferInformation import BufferInformation


class HaapiBufferListMessage(INetworkMessage):
    protocolId = 518
    buffers:BufferInformation
    
    
