from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuestLimitationMessage(INetworkMessage):
    protocolId = 1036
    reason:int
    
    
