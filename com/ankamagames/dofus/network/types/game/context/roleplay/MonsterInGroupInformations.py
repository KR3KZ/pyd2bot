from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class MonsterInGroupInformations(MonsterInGroupLightInformations):
    look:'EntityLook'
    

    def init(self, look:'EntityLook', genericId:int, grade:int, level:int):
        self.look = look
        
        super().__init__(genericId, grade, level)
    
    