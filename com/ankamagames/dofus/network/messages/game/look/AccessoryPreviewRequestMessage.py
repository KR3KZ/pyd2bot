from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AccessoryPreviewRequestMessage(NetworkMessage):
    protocolId = 35
    genericId:int
    
    
