from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicWhoAmIRequestMessage(INetworkMessage):
    protocolId = 1281
    verbose:bool
    
    
