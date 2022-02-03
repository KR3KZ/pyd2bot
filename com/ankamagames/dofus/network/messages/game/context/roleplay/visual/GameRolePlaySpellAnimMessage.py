from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlaySpellAnimMessage(NetworkMessage):
    casterId:int
    targetCellId:int
    spellId:int
    spellLevel:int
    

    def init(self, casterId_:int, targetCellId_:int, spellId_:int, spellLevel_:int):
        self.casterId = casterId_
        self.targetCellId = targetCellId_
        self.spellId = spellId_
        self.spellLevel = spellLevel_
        
        super().__init__()
    
    