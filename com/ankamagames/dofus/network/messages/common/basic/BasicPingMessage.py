from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BasicPingMessage(INetworkMessage):
    protocolId = 8161
    quiet:bool
    
    
