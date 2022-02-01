from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyMemberRemoveMessage import PartyMemberRemoveMessage


class PartyMemberEjectedMessage(PartyMemberRemoveMessage):
    kickerId:int
    
    
