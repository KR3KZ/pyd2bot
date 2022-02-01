from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill


class InteractiveElement(NetworkMessage):
    elementId:int
    elementTypeId:int
    enabledSkills:list[InteractiveElementSkill]
    disabledSkills:list[InteractiveElementSkill]
    onCurrentMap:bool
    
    
