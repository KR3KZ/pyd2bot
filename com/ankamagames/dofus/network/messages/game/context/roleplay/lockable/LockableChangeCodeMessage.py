from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LockableChangeCodeMessage(NetworkMessage):
    protocolId = 768
    code:str
    
    
