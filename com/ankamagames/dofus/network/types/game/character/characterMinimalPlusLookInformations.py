from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterMinimalPlusLookInformations(CharacterMinimalInformations):
    entityLook:'EntityLook'
    breed:int
    

    def init(self, entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.entityLook = entityLook
        self.breed = breed
        
        super().__init__(level, name, id)
    
    