from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescriptionTimed import SkillActionDescriptionTimed


class SkillActionDescriptionCollect(SkillActionDescriptionTimed):
    min:int
    max:int
    

    def init(self, min:int, max:int, time:int, skillId:int):
        self.min = min
        self.max = max
        
        super().__init__(time, skillId)
    
    