from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElementSkill import InteractiveElementSkill


class InteractiveElement(NetworkMessage):
    protocolId = 4768
    elementId:int
    elementTypeId:int
    enabledSkills:InteractiveElementSkill
    disabledSkills:InteractiveElementSkill
    onCurrentMap:bool
    
