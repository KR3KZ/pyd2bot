from com.ankamagames.dofus.network.messages.game.context.roleplay.party.PartyUpdateLightMessage import PartyUpdateLightMessage


class PartyEntityUpdateLightMessage(PartyUpdateLightMessage):
    indexId:int
    

    def init(self, indexId:int, id:int, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, partyId:int):
        self.indexId = indexId
        
        super().__init__(id, lifePoints, maxLifePoints, prospecting, regenRate, partyId)
    
    