from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LockableUseCodeMessage(INetworkMessage):
    protocolId = 5618
    code:str
    
    
