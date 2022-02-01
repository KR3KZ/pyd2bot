from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ReloginTokenStatusMessage(INetworkMessage):
    protocolId = 3172
    validToken:bool
    ticket:int
    
    
