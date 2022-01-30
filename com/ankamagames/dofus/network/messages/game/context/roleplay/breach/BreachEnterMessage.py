from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BreachEnterMessage(NetworkMessage):
    protocolId = 6485
    owner:float
    
