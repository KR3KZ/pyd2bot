from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationRequestMessage import PartyInvitationRequestMessage


class PartyInvitationDungeonRequestMessage(PartyInvitationRequestMessage):
    protocolId = 8333
    dungeonId:int
    
    
