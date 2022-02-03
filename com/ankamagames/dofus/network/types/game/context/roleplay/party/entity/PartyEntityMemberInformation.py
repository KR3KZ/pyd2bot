from com.ankamagames.dofus.network.types.game.context.roleplay.party.entity.PartyEntityBaseInformation import PartyEntityBaseInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class PartyEntityMemberInformation(PartyEntityBaseInformation):
    initiative:int
    lifePoints:int
    maxLifePoints:int
    prospecting:int
    regenRate:int
    

    def init(self, initiative:int, lifePoints:int, maxLifePoints:int, prospecting:int, regenRate:int, indexId:int, entityModelId:int, entityLook:'EntityLook'):
        self.initiative = initiative
        self.lifePoints = lifePoints
        self.maxLifePoints = maxLifePoints
        self.prospecting = prospecting
        self.regenRate = regenRate
        
        super().__init__(indexId, entityModelId, entityLook)
    
    