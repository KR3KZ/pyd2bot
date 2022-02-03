from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationMessage import PartyInvitationMessage


class PartyInvitationDungeonMessage(PartyInvitationMessage):
    dungeonId:int
    

    def init(self, dungeonId:int, partyType:int, partyName:str, maxParticipants:int, fromId:int, fromName:str, toId:int, partyId:int):
        self.dungeonId = dungeonId
        
        super().__init__(partyType, partyName, maxParticipants, fromId, fromName, toId, partyId)
    
    