from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LockableStateUpdateAbstractMessage(NetworkMessage):
    protocolId = 5676
    locked:bool
    
