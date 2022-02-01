from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage


class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
    playerId:int
    skills:list[int]
    
    
