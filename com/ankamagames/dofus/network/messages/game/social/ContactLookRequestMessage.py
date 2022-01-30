from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ContactLookRequestMessage(INetworkMessage):
    protocolId = 9165
    requestId:int
    contactType:int
    
    
