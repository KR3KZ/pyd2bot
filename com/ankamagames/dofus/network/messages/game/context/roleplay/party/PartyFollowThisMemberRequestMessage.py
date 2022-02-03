from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyFollowMemberRequestMessage import PartyFollowMemberRequestMessage


class PartyFollowThisMemberRequestMessage(PartyFollowMemberRequestMessage):
    enabled:bool
    

    def init(self, enabled:bool, playerId:int, partyId:int):
        self.enabled = enabled
        
        super().__init__(playerId, partyId)
    
    