from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectErrorMessage(INetworkMessage):
    protocolId = 9603
    reason:int
    
    
