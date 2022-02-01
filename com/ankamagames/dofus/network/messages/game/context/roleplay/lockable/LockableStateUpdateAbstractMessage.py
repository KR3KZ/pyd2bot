from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LockableStateUpdateAbstractMessage(INetworkMessage):
    protocolId = 5676
    locked:bool
    
    
