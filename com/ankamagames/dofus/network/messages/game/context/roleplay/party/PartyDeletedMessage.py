from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyDeletedMessage(AbstractPartyMessage):
    

    def init(self, partyId:int):
        
        super().__init__(partyId)
    
    