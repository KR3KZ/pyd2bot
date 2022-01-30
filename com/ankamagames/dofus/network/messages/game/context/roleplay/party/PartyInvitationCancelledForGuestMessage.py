from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationCancelledForGuestMessage(AbstractPartyMessage):
    protocolId = 1943
    cancelerId:float
    
