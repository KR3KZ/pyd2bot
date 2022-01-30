from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyPledgeLoyaltyRequestMessage(AbstractPartyMessage):
    protocolId = 8034
    loyal:bool
    
    
