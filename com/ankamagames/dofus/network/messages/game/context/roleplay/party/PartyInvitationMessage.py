from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationMessage(AbstractPartyMessage):
    protocolId = 1660
    partyType:int
    partyName:str
    maxParticipants:int
    fromId:int
    fromName:str
    toId:int
    
    
