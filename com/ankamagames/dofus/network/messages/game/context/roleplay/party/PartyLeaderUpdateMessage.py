from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyLeaderUpdateMessage(AbstractPartyEventMessage):
    protocolId = 4003
    partyLeaderId:float
    
