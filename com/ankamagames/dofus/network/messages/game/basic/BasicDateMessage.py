from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicDateMessage(INetworkMessage):
    protocolId = 4911
    day:int
    month:int
    year:int
    
    
