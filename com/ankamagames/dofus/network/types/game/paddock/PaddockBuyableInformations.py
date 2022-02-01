from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockBuyableInformations(INetworkMessage):
    protocolId = 3536
    price:int
    locked:bool
    
    
