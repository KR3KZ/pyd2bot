from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuestModeMessage(NetworkMessage):
    protocolId = 9430
    active:bool
    
    
