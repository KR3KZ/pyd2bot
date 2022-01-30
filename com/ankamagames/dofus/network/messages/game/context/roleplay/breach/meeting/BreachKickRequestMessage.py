from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachKickRequestMessage(NetworkMessage):
    protocolId = 2909
    target:int
    
