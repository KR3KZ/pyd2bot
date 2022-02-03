from com.ankamagames.dofus.network.types.game.character.choice.CharacterRemodelingInformation import CharacterRemodelingInformation


class CharacterToRemodelInformations(CharacterRemodelingInformation):
    possibleChangeMask:int
    mandatoryChangeMask:int
    

    def init(self, possibleChangeMask:int, mandatoryChangeMask:int, name:str, breed:int, sex:bool, cosmeticId:int, colors:list[int], id:int):
        self.possibleChangeMask = possibleChangeMask
        self.mandatoryChangeMask = mandatoryChangeMask
        
        super().__init__(name, breed, sex, cosmeticId, colors, id)
    
    