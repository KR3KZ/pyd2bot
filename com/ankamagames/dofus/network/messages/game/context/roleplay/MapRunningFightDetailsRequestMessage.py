from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MapRunningFightDetailsRequestMessage(INetworkMessage):
    protocolId = 8028
    fightId:int
    
    
