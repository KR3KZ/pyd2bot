from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyNameSetRequestMessage(AbstractPartyMessage):
    protocolId = 3956
    partyName:str
    
    
