from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ContactAddFailureMessage(NetworkMessage):
    protocolId = 7999
    reason:int
    
