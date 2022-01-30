from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LockableStateUpdateAbstractMessage(INetworkMessage):
    protocolId = 5676
    locked:bool
    
    
