from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
    followedId:int
    success:bool
    isFollowed:bool
    

    def init(self, followedId:int, partyId:int):
        self.followedId = followedId
        
        super().__init__(partyId)
    
    