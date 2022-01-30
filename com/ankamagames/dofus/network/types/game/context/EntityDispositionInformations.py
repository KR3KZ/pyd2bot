from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EntityDispositionInformations(NetworkMessage):
    protocolId = 7424
    cellId:int
    direction:int
    
    
