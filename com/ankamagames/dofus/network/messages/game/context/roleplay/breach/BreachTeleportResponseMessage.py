from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachTeleportResponseMessage(NetworkMessage):
    protocolId = 4766
    teleported:bool
    
    
