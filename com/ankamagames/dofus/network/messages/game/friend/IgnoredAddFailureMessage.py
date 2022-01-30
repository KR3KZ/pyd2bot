from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class IgnoredAddFailureMessage(INetworkMessage):
    protocolId = 4052
    reason:int
    
    
