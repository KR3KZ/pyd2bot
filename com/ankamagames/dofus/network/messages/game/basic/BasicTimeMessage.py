from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicTimeMessage(INetworkMessage):
    protocolId = 7278
    timestamp:int
    timezoneOffset:int
    
    
