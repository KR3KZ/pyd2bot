from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterBaseInformations(CharacterMinimalPlusLookInformations):
    sex:bool
    

    def init(self, sex:bool, entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.sex = sex
        
        super().__init__(entityLook, breed, level, name, id)
    
    