from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class BasicStatMessage(INetworkMessage):
    protocolId = 514
    timeSpent:int
    statId:int
    
    
