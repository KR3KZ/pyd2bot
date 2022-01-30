from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StorageKamasUpdateMessage(NetworkMessage):
    protocolId = 4689
    kamasTotal:float
    
