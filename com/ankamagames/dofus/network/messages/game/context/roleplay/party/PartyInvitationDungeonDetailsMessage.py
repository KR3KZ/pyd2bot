from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDetailsMessage import PartyInvitationDetailsMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyInvitationMemberInformations import PartyInvitationMemberInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations
    


class PartyInvitationDungeonDetailsMessage(PartyInvitationDetailsMessage):
    dungeonId:int
    playersDungeonReady:list[bool]
    

    def init(self, dungeonId:int, playersDungeonReady:list[bool], partyType:int, partyName:str, fromId:int, fromName:str, leaderId:int, members:list['PartyInvitationMemberInformations'], guests:list['PartyGuestInformations'], partyId:int):
        self.dungeonId = dungeonId
        self.playersDungeonReady = playersDungeonReady
        
        super().__init__(partyType, partyName, fromId, fromName, leaderId, members, guests, partyId)
    
    