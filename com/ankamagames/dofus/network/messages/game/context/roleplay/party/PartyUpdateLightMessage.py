from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyUpdateLightMessage(AbstractPartyEventMessage):
    protocolId = 585
    id:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    
    
