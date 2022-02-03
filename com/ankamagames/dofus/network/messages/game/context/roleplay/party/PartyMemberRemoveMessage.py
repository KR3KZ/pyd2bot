from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyMemberRemoveMessage(AbstractPartyEventMessage):
    leavingPlayerId:int
    

    def init(self, leavingPlayerId:int, partyId:int):
        self.leavingPlayerId = leavingPlayerId
        
        super().__init__(partyId)
    
    