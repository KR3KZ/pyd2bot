from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MapObstacle(NetworkMessage):
    protocolId = 5512
    obstacleCellId:int
    state:int
    
    
