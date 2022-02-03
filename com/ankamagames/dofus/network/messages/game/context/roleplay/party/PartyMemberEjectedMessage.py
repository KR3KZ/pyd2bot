from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberRemoveMessage import PartyMemberRemoveMessage


class PartyMemberEjectedMessage(PartyMemberRemoveMessage):
    kickerId:int
    

    def init(self, kickerId:int, leavingPlayerId:int, partyId:int):
        self.kickerId = kickerId
        
        super().__init__(leavingPlayerId, partyId)
    
    