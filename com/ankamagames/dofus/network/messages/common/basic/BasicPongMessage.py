from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BasicPongMessage(INetworkMessage):
    protocolId = 2330
    quiet:bool
    
    
