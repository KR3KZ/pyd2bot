from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntFlag(INetworkMessage):
    protocolId = 4191
    mapId:int
    state:int
    
    
