from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightNoSpellCastMessage(NetworkMessage):
    spellLevelId:int
    

    def init(self, spellLevelId:int):
        self.spellLevelId = spellLevelId
        
        super().__init__()
    
    