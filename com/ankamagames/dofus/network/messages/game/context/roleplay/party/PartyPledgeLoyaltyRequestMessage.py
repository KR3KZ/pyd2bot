from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyPledgeLoyaltyRequestMessage(AbstractPartyMessage):
    loyal:bool
    

    def init(self, loyal:bool, partyId:int):
        self.loyal = loyal
        
        super().__init__(partyId)
    
    