from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDetailsMessage import PartyInvitationDetailsMessage


class PartyInvitationDungeonDetailsMessage(PartyInvitationDetailsMessage):
    protocolId = 7340
    dungeonId:int
    playersDungeonReady:bool
    
    
