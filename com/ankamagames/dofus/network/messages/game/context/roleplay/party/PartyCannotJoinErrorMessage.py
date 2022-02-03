from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyCannotJoinErrorMessage(AbstractPartyMessage):
    reason:int
    

    def init(self, reason:int, partyId:int):
        self.reason = reason
        
        super().__init__(partyId)
    
    