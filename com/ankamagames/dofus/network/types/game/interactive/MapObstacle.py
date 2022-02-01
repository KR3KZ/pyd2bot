from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MapObstacle(INetworkMessage):
    protocolId = 5512
    obstacleCellId:int
    state:int
    
    
