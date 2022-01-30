from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IdolSelectErrorMessage(NetworkMessage):
    protocolId = 4378
    reason:int
    idolId:int
    
