from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.skill.SkillActionDescription import SkillActionDescription


class JobDescription(INetworkMessage):
    protocolId = 2005
    jobId:int
    skills:SkillActionDescription
    
    
