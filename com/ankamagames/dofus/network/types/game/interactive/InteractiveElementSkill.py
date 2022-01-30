from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class InteractiveElementSkill(INetworkMessage):
    protocolId = 6784
    skillId:int
    skillInstanceUid:int
    
    
