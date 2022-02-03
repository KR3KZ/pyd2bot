from com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation


class SpawnMonsterInformation(BaseSpawnMonsterInformation):
    creatureGrade:int
    

    def init(self, creatureGrade:int, creatureGenericId:int):
        self.creatureGrade = creatureGrade
        
        super().__init__(creatureGenericId)
    
    