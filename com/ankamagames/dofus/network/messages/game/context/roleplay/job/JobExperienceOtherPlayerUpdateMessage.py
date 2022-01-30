from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobExperienceUpdateMessage import JobExperienceUpdateMessage


class JobExperienceOtherPlayerUpdateMessage(JobExperienceUpdateMessage):
    protocolId = 5477
    playerId:int
    
    
