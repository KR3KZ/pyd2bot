from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyNameUpdateMessage(AbstractPartyMessage):
    protocolId = 4910
    partyName:str
    
    
