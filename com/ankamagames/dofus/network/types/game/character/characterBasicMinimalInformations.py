from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


class CharacterBasicMinimalInformations(AbstractCharacterInformation):
    name:str
    

    def init(self, name:str, id:int):
        self.name = name
        
        super().__init__(id)
    
    