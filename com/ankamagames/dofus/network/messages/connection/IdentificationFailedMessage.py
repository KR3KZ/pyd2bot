from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class IdentificationFailedMessage(INetworkMessage):
    protocolId = 7135
    reason:int
    
    
