from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LockableCodeResultMessage(NetworkMessage):
    protocolId = 3222
    result:int
    
    
