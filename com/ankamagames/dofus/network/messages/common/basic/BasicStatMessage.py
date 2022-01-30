from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class BasicStatMessage(NetworkMessage):
    protocolId = 514
    timeSpent:int
    statId:int
    
