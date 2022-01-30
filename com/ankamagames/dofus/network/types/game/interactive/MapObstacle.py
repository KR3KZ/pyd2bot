from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MapObstacle(INetworkMessage):
    protocolId = 5512
    obstacleCellId:int
    state:int
    
    
