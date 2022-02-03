from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
    


class InteractiveElement(NetworkMessage):
    elementId:int
    elementTypeId:int
    enabledSkills:list['InteractiveElementSkill']
    disabledSkills:list['InteractiveElementSkill']
    onCurrentMap:bool
    

    def init(self, elementId:int, elementTypeId:int, enabledSkills:list['InteractiveElementSkill'], disabledSkills:list['InteractiveElementSkill'], onCurrentMap:bool):
        self.elementId = elementId
        self.elementTypeId = elementTypeId
        self.enabledSkills = enabledSkills
        self.disabledSkills = disabledSkills
        self.onCurrentMap = onCurrentMap
        
        super().__init__()
    
    