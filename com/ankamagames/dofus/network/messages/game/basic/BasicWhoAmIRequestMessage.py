from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicWhoAmIRequestMessage(NetworkMessage):
    protocolId = 1281
    verbose:bool
    
    
