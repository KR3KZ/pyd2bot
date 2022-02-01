from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildChangeMemberParametersMessage(NetworkMessage):
    memberId:int
    rank:int
    experienceGivenPercent:int
    rights:int
    
    
