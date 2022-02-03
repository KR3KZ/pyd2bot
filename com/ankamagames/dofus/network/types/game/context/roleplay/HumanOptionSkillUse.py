from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


class HumanOptionSkillUse(HumanOption):
    elementId:int
    skillId:int
    skillEndTime:int
    

    def init(self, elementId:int, skillId:int, skillEndTime:int):
        self.elementId = elementId
        self.skillId = skillId
        self.skillEndTime = skillEndTime
        
        super().__init__()
    
    