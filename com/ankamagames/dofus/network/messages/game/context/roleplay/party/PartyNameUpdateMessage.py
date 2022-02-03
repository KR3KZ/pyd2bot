from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyNameUpdateMessage(AbstractPartyMessage):
    partyName:str
    

    def init(self, partyName:str, partyId:int):
        self.partyName = partyName
        
        super().__init__(partyId)
    
    