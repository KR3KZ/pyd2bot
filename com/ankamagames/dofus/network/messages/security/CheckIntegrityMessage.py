from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CheckIntegrityMessage(NetworkMessage):
    protocolId = 1296
    data:int
    
    
