from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMountSterilizeFromPaddockMessage(NetworkMessage):
    name:str
    worldX:int
    worldY:int
    sterilizator:str
    

    def init(self, name:str, worldX:int, worldY:int, sterilizator:str):
        self.name = name
        self.worldX = worldX
        self.worldY = worldY
        self.sterilizator = sterilizator
        
        super().__init__()
    
    