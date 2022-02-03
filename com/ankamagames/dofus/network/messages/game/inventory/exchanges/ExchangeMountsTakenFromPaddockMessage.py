from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountsTakenFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    ownername:str
    

    def init(self, name:str, worldX:int, worldY:int, ownername:str):
        self.name = name
        self.worldX = worldX
        self.worldY = worldY
        self.ownername = ownername
        
        super().__init__()
    
    