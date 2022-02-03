from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyKickRequestMessage(AbstractPartyMessage):
    playerId:int
    

    def init(self, playerId:int, partyId:int):
        self.playerId = playerId
        
        super().__init__(partyId)
    
    