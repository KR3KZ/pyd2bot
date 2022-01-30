from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicDateMessage(NetworkMessage):
    protocolId = 4911
    day:int
    month:int
    year:int
    
    
