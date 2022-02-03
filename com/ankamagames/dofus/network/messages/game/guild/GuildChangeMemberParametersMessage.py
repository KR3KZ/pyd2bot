from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildChangeMemberParametersMessage(NetworkMessage):
    memberId:int
    rank:int
    experienceGivenPercent:int
    rights:int
    

    def init(self, memberId:int, rank:int, experienceGivenPercent:int, rights:int):
        self.memberId = memberId
        self.rank = rank
        self.experienceGivenPercent = experienceGivenPercent
        self.rights = rights
        
        super().__init__()
    
    