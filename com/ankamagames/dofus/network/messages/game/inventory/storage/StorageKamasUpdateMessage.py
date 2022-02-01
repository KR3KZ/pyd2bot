from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class StorageKamasUpdateMessage(INetworkMessage):
    protocolId = 4689
    kamasTotal:int
    
    
