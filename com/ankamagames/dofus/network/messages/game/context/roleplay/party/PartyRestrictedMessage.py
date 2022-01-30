from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyRestrictedMessage(AbstractPartyMessage):
    protocolId = 6433
    restricted:bool
    
