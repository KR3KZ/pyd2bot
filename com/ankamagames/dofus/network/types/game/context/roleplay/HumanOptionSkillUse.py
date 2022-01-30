from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionSkillUse(HumanOption):
    protocolId = 2427
    elementId:int
    skillId:int
    skillEndTime:int
    
    
