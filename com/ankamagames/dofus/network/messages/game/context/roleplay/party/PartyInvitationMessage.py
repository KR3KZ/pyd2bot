from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationMessage(AbstractPartyMessage):
    partyType:int
    partyName:str
    maxParticipants:int
    fromId:int
    fromName:str
    toId:int
    

    def init(self, partyType:int, partyName:str, maxParticipants:int, fromId:int, fromName:str, toId:int, partyId:int):
        self.partyType = partyType
        self.partyName = partyName
        self.maxParticipants = maxParticipants
        self.fromId = fromId
        self.fromName = fromName
        self.toId = toId
        
        super().__init__(partyId)
    
    