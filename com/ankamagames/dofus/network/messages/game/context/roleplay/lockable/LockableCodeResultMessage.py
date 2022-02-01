from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LockableCodeResultMessage(INetworkMessage):
    protocolId = 3222
    result:int
    
    
