from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachSavedMessage(NetworkMessage):
    protocolId = 4537
    saved:bool
    
