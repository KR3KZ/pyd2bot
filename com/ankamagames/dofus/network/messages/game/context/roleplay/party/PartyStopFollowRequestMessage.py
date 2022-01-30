from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyStopFollowRequestMessage(AbstractPartyMessage):
    protocolId = 9834
    playerId:int
    
    
