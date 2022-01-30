from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage


class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
    protocolId = 1246
    playerId:int
    skills:int
    
    
