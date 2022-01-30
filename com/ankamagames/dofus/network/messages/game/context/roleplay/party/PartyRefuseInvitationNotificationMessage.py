from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyRefuseInvitationNotificationMessage(AbstractPartyEventMessage):
    protocolId = 349
    guestId:int
    
    
