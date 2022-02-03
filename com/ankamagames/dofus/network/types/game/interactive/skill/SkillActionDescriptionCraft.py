from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


class SkillActionDescriptionCraft(SkillActionDescription):
    probability:int
    

    def init(self, probability:int, skillId:int):
        self.probability = probability
        
        super().__init__(skillId)
    
    