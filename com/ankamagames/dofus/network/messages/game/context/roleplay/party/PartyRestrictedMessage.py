from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyRestrictedMessage(AbstractPartyMessage):
    restricted:bool
    

    def init(self, restricted:bool, partyId:int):
        self.restricted = restricted
        
        super().__init__(partyId)
    
    