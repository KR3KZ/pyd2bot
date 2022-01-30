from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyModifiableStatusMessage(AbstractPartyMessage):
    protocolId = 4439
    enabled:bool
    
