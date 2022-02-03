from com.ankamagames.dofus.network.types.game.character.choice.CharacterBaseInformations import CharacterBaseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterHardcoreOrEpicInformations(CharacterBaseInformations):
    deathState:int
    deathCount:int
    deathMaxLevel:int
    

    def init(self, deathState:int, deathCount:int, deathMaxLevel:int, sex:bool, entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.deathState = deathState
        self.deathCount = deathCount
        self.deathMaxLevel = deathMaxLevel
        
        super().__init__(sex, entityLook, breed, level, name, id)
    
    