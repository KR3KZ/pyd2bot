from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class RecycleResultMessage(INetworkMessage):
    protocolId = 2853
    nuggetsForPrism:int
    nuggetsForPlayer:int
    
    
