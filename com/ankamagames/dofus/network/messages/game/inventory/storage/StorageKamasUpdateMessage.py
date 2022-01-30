from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StorageKamasUpdateMessage(INetworkMessage):
    protocolId = 4689
    kamasTotal:int
    
    
