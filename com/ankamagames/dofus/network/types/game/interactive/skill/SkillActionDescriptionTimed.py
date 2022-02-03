from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


class SkillActionDescriptionTimed(SkillActionDescription):
    time:int
    

    def init(self, time:int, skillId:int):
        self.time = time
        
        super().__init__(skillId)
    
    