from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyKickedByMessage(AbstractPartyMessage):
    kickerId:int
    

    def init(self, kickerId:int, partyId:int):
        self.kickerId = kickerId
        
        super().__init__(partyId)
    
    