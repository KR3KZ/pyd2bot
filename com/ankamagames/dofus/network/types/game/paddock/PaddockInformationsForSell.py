from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockInformationsForSell(NetworkMessage):
    guildOwner:str
    worldX:int
    worldY:int
    subAreaId:int
    nbMount:int
    nbObject:int
    price:int
    

    def init(self, guildOwner:str, worldX:int, worldY:int, subAreaId:int, nbMount:int, nbObject:int, price:int):
        self.guildOwner = guildOwner
        self.worldX = worldX
        self.worldY = worldY
        self.subAreaId = subAreaId
        self.nbMount = nbMount
        self.nbObject = nbObject
        self.price = price
        
        super().__init__()
    
    