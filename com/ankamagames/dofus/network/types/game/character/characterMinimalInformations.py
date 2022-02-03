from com.ankamagames.dofus.network.types.game.character.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations


class CharacterMinimalInformations(CharacterBasicMinimalInformations):
    level:int
    

    def init(self, level:int, name:str, id:int):
        self.level = level
        
        super().__init__(name, id)
    
    