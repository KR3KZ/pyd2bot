from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IdolSelectRequestMessage(NetworkMessage):
    protocolId = 5093
    idolId:int
    
