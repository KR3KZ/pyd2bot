from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountDataErrorMessage(INetworkMessage):
    protocolId = 24
    reason:int
    
    
