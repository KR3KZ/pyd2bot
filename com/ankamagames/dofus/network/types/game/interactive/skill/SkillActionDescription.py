from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SkillActionDescription(INetworkMessage):
    protocolId = 2262
    skillId:int
    
    
