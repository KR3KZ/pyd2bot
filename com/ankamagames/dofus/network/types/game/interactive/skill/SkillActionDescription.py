from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SkillActionDescription(INetworkMessage):
    protocolId = 2262
    skillId:int
    
    
