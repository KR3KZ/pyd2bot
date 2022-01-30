from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class InteractiveElementSkill(NetworkMessage):
    protocolId = 6784
    skillId:int
    skillInstanceUid:int
    
