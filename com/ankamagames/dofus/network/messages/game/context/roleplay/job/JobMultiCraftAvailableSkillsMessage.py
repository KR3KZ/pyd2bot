from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.job.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage


@dataclass
class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
    playerId:int
    skills:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    