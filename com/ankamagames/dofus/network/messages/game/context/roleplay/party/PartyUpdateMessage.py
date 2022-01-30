from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyMemberInformations import PartyMemberInformations


class PartyUpdateMessage(AbstractPartyEventMessage):
    protocolId = 1769
    memberInformations:PartyMemberInformations
    
    
