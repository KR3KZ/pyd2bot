from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TitlesAndOrnamentsListMessage(INetworkMessage):
    protocolId = 6204
    titles:int
    ornaments:int
    activeTitle:int
    activeOrnament:int
    
    
