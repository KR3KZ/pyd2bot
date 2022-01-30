from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ReloginTokenStatusMessage(INetworkMessage):
    protocolId = 3172
    validToken:bool
    ticket:int
    
    
