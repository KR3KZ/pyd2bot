from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyCancelInvitationMessage(AbstractPartyMessage):
    protocolId = 7066
    guestId:float
    
