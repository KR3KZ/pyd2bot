from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DecraftedItemStackInfo(NetworkMessage):
    objectUID:int
    bonusMin:int
    bonusMax:int
    runesId:list[int]
    runesQty:list[int]
    

    def init(self, objectUID:int, bonusMin:int, bonusMax:int, runesId:list[int], runesQty:list[int]):
        self.objectUID = objectUID
        self.bonusMin = bonusMin
        self.bonusMax = bonusMax
        self.runesId = runesId
        self.runesQty = runesQty
        
        super().__init__()
    
    