from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.party.PartyGuestInformations import PartyGuestInformations


class PartyNewGuestMessage(AbstractPartyEventMessage):
    protocolId = 1263
    guest:PartyGuestInformations
    
