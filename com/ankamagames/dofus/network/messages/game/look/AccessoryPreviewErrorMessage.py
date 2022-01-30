from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AccessoryPreviewErrorMessage(INetworkMessage):
    protocolId = 2038
    error:int
    
    
