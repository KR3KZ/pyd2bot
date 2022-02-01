from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MapRunningFightDetailsRequestMessage(INetworkMessage):
    protocolId = 8028
    fightId:int
    
    
