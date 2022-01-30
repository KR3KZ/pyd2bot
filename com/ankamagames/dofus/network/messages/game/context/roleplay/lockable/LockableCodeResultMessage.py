from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LockableCodeResultMessage(INetworkMessage):
    protocolId = 3222
    result:int
    
    
