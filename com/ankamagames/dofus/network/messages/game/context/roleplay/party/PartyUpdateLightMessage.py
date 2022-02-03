from com.ankamagames.dofus.network.messages.game.context.roleplay.party.AbstractPartyEventMessage import AbstractPartyEventMessage


class PartyUpdateLightMessage(AbstractPartyEventMessage):
    id:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    

    def init(self, id:int, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, partyId:int):
        self.id = id
        self.lifePoints = lifePoints
        self.maxLifePoints = maxLifePoints
        self.prospecting = prospecting
        self.regenRate = regenRate
        
        super().__init__(partyId)
    
    