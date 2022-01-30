from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LockableUseCodeMessage(NetworkMessage):
    protocolId = 5618
    code:str
    
    
