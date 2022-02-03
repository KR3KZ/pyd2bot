from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    


class InteractiveElementWithAgeBonus(InteractiveElement):
    ageBonus:int
    

    def init(self, ageBonus:int, elementId:int, elementTypeId:int, enabledSkills:list['InteractiveElementSkill'], disabledSkills:list['InteractiveElementSkill'], onCurrentMap:bool):
        self.ageBonus = ageBonus
        
        super().__init__(elementId, elementTypeId, enabledSkills, disabledSkills, onCurrentMap)
    
    