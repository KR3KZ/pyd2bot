from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage


class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
    protocolId = 9876
    floor:int
    room:int
    
