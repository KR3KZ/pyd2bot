from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ContactLookRequestMessage(NetworkMessage):
    protocolId = 9165
    requestId:int
    contactType:int
    
