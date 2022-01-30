from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IdolSelectedMessage(NetworkMessage):
    protocolId = 7348
    idolId:int
    
