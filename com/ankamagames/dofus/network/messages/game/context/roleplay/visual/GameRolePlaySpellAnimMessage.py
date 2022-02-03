from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlaySpellAnimMessage(NetworkMessage):
    casterId:int
    targetCellId:int
    spellId:int
    spellLevel:int
    

    def init(self, casterId:int, targetCellId:int, spellId:int, spellLevel:int):
        self.casterId = casterId
        self.targetCellId = targetCellId
        self.spellId = spellId
        self.spellLevel = spellLevel
        
        super().__init__()
    
    