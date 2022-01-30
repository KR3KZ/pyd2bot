from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachExitResponseMessage(NetworkMessage):
    protocolId = 7143
    exited:bool
    
