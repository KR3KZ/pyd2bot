from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class KamasUpdateMessage(INetworkMessage):
    protocolId = 4370
    kamasTotal:int
    
    
