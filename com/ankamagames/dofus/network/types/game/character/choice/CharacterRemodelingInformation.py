from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


class CharacterRemodelingInformation(AbstractCharacterInformation):
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:list[int]
    
    
