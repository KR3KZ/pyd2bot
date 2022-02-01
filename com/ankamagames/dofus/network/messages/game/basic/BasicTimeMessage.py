from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class BasicTimeMessage(INetworkMessage):
    protocolId = 7278
    timestamp:int
    timezoneOffset:int
    
    
