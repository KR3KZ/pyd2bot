from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class KamasUpdateMessage(NetworkMessage):
    protocolId = 4370
    kamasTotal:int
    
    
