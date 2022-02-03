from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountFreeFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    liberator:str
    

    def init(self, name:str, worldX:int, worldY:int, liberator:str):
        self.name = name
        self.worldX = worldX
        self.worldY = worldY
        self.liberator = liberator
        
        super().__init__()
    
    