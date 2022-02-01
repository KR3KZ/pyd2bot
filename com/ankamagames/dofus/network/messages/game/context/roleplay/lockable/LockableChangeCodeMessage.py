from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LockableChangeCodeMessage(INetworkMessage):
    protocolId = 768
    code:str
    
    
