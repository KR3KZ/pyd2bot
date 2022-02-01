from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyUpdateLightMessage(AbstractPartyEventMessage):
    id:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    
    
