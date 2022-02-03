from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapCoordinates(NetworkMessage):
    worldX:int
    worldY:int
    

    def init(self, worldX:int, worldY:int):
        self.worldX = worldX
        self.worldY = worldY
        
        super().__init__()
    
    