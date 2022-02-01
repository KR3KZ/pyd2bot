from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildChangeMemberParametersMessage(INetworkMessage):
    protocolId = 3633
    memberId:int
    rank:int
    experienceGivenPercent:int
    rights:int
    
    
