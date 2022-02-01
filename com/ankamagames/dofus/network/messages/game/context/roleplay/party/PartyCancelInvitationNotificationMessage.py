from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
    cancelerId:int
    guestId:int
    
    
