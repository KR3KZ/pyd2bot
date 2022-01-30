from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SkillActionDescription(NetworkMessage):
    protocolId = 2262
    skillId:int
    
