from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyCannotJoinErrorMessage(AbstractPartyMessage):
    protocolId = 8807
    reason:int
    
    
