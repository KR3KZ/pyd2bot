from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildChangeMemberParametersMessage(NetworkMessage):
    protocolId = 3633
    memberId:int
    rank:int
    experienceGivenPercent:int
    rights:int
    
    
