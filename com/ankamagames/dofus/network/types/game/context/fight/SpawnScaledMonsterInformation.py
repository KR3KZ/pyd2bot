from com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation


class SpawnScaledMonsterInformation(BaseSpawnMonsterInformation):
    creatureLevel:int
    

    def init(self, creatureLevel:int, creatureGenericId:int):
        self.creatureLevel = creatureLevel
        
        super().__init__(creatureGenericId)
    
    