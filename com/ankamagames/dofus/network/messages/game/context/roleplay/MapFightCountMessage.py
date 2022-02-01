from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MapFightCountMessage(INetworkMessage):
    protocolId = 9018
    fightCount:int
    
    
