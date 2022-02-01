from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyInvitationDetailsMessage import PartyInvitationDetailsMessage


class PartyInvitationDungeonDetailsMessage(PartyInvitationDetailsMessage):
    dungeonId:int
    playersDungeonReady:list[bool]
    
    
