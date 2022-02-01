from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class OrnamentSelectErrorMessage(INetworkMessage):
    protocolId = 4098
    reason:int
    
    
