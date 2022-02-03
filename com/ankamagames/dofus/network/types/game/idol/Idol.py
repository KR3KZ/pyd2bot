from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class Idol(NetworkMessage):
    id:int
    xpBonusPercent:int
    dropBonusPercent:int
    

    def init(self, id:int, xpBonusPercent:int, dropBonusPercent:int):
        self.id = id
        self.xpBonusPercent = xpBonusPercent
        self.dropBonusPercent = dropBonusPercent
        
        super().__init__()
    
    