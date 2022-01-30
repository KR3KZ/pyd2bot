from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
    protocolId = 1489
    cancelerId:int
    guestId:int
    
