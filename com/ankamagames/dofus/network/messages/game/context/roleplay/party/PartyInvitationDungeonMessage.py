from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationMessage import PartyInvitationMessage


class PartyInvitationDungeonMessage(PartyInvitationMessage):
    protocolId = 9837
    dungeonId:int
    
    
