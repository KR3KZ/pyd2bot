from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyAbdicateThroneMessage(AbstractPartyMessage):
    protocolId = 6752
    playerId:int
    
    
