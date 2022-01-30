from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ContactAddFailureMessage(INetworkMessage):
    protocolId = 7999
    reason:int
    
    
