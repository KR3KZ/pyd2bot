from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyNameSetErrorMessage(AbstractPartyMessage):
    protocolId = 9899
    result:int
    
