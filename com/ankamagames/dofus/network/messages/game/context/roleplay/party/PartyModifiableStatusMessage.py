from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyModifiableStatusMessage(AbstractPartyMessage):
    enabled:bool
    

    def init(self, enabled:bool, partyId:int):
        self.enabled = enabled
        
        super().__init__(partyId)
    
    