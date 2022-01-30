from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyLoyaltyStatusMessage(AbstractPartyMessage):
    protocolId = 5410
    loyal:bool
    
    
