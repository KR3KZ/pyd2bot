from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyLeaderUpdateMessage(AbstractPartyEventMessage):
    partyLeaderId:int
    

    def init(self, partyLeaderId:int, partyId:int):
        self.partyLeaderId = partyLeaderId
        
        super().__init__(partyId)
    
    