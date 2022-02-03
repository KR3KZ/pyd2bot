from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyNameSetErrorMessage(AbstractPartyMessage):
    result:int
    

    def init(self, result:int, partyId:int):
        self.result = result
        
        super().__init__(partyId)
    
    