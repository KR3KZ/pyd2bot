from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LoginQueueStatusMessage(INetworkMessage):
    protocolId = 2063
    position:int
    total:int
    
    
