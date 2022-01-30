from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class IdolPartyRegisterRequestMessage(NetworkMessage):
    protocolId = 868
    register:bool
    
    
