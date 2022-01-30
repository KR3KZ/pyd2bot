from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AccessoryPreviewErrorMessage(NetworkMessage):
    protocolId = 2038
    error:int
    
