from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill


@dataclass
class InteractiveElement(NetworkMessage):
    elementId:int
    elementTypeId:int
    enabledSkills:list[InteractiveElementSkill]
    disabledSkills:list[InteractiveElementSkill]
    onCurrentMap:bool
    
    
    def __post_init__(self):
        super().__init__()
    