from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyMessage import AbstractPartyMessage


class PartyKickRequestMessage(AbstractPartyMessage):
    protocolId = 6075
    playerId:float
    
