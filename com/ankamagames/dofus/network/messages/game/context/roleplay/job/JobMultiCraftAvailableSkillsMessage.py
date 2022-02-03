from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage


class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
    playerId:int
    skills:list[int]
    

    def init(self, playerId:int, skills:list[int], enabled:bool):
        self.playerId = playerId
        self.skills = skills
        
        super().__init__(enabled)
    
    