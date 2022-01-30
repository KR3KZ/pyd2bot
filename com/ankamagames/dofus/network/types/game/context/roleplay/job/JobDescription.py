from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


class JobDescription(NetworkMessage):
    protocolId = 2005
    jobId:int
    skills:list[SkillActionDescription]
    
