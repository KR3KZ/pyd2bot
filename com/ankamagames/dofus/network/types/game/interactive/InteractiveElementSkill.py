from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class InteractiveElementSkill(INetworkMessage):
    protocolId = 6784
    skillId:int
    skillInstanceUid:int
    
    
