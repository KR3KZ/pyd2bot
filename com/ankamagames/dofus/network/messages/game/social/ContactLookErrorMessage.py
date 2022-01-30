from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ContactLookErrorMessage(NetworkMessage):
    protocolId = 9873
    requestId:int
    
