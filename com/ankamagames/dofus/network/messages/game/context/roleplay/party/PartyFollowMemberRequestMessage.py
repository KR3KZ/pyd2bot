from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyFollowMemberRequestMessage(AbstractPartyMessage):
    protocolId = 8603
    playerId:int
    
    
