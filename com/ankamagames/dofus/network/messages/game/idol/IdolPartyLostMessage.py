from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IdolPartyLostMessage(NetworkMessage):
    protocolId = 7502
    idolId:int
    
