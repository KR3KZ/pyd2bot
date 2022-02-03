from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapObstacle(NetworkMessage):
    obstacleCellId:int
    state:int
    

    def init(self, obstacleCellId:int, state:int):
        self.obstacleCellId = obstacleCellId
        self.state = state
        
        super().__init__()
    
    