from com.ankamagames.dofus.network.types.game.character.AbstractCharacterInformation import AbstractCharacterInformation


class CharacterRemodelingInformation(AbstractCharacterInformation):
    protocolId = 5402
    name:str
    breed:int
    sex:bool
    cosmeticId:int
    colors:int
    
