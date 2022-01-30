from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AccessoryPreviewRequestMessage(INetworkMessage):
    protocolId = 35
    genericId:int
    
    
