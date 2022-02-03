from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


class CharacterRemodelingInformation(AbstractCharacterInformation):
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:list[int]
    

    def init(self, name:str, breed:int, sex:bool, cosmeticId:int, colors:list[int], id:int):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.cosmeticId = cosmeticId
        self.colors = colors
        
        super().__init__(id)
    
    