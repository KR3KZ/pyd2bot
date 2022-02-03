from com.ankamagames.dofus.network.types.game.character.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class CharacterMinimalPlusLookAndGradeInformations(CharacterMinimalPlusLookInformations):
    grade:int
    

    def init(self, grade:int, entityLook:'EntityLook', breed:int, level:int, name:str, id:int):
        self.grade = grade
        
        super().__init__(entityLook, breed, level, name, id)
    
    