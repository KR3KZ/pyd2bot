from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ChatErrorMessage(INetworkMessage):
    protocolId = 5479
    reason:int
    
    
