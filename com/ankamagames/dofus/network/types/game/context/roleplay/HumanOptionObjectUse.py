from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionObjectUse(HumanOption):
    delayTypeId:int
    delayEndTime:int
    objectGID:int
    

    def init(self, delayTypeId:int, delayEndTime:int, objectGID:int):
        self.delayTypeId = delayTypeId
        self.delayEndTime = delayEndTime
        self.objectGID = objectGID
        
        super().__init__()
    
    