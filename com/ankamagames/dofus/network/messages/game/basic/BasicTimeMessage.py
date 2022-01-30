from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicTimeMessage(NetworkMessage):
    protocolId = 7278
    timestamp:int
    timezoneOffset:int
    
    
