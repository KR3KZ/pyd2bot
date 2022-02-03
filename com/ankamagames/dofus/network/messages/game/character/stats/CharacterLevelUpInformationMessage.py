from com.ankamagames.dofus.network.messages.game.character.stats.CharacterLevelUpMessage import CharacterLevelUpMessage


class CharacterLevelUpInformationMessage(CharacterLevelUpMessage):
    name:str
    id:int
    

    def init(self, name:str, id:int, newLevel:int):
        self.name = name
        self.id = id
        
        super().__init__(newLevel)
    
    