from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ContactLookErrorMessage(INetworkMessage):
    protocolId = 9873
    requestId:int
    
    
