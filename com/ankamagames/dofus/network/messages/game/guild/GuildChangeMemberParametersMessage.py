from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildChangeMemberParametersMessage(NetworkMessage):
    memberId:int
    rank:int
    experienceGivenPercent:int
    rights:int
    

    def init(self, memberId_:int, rank_:int, experienceGivenPercent_:int, rights_:int):
        self.memberId = memberId_
        self.rank = rank_
        self.experienceGivenPercent = experienceGivenPercent_
        self.rights = rights_
        
        super().__init__()
    
    