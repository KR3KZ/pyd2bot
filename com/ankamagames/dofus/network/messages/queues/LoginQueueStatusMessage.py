from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LoginQueueStatusMessage(INetworkMessage):
    protocolId = 2063
    position:int
    total:int
    
    
