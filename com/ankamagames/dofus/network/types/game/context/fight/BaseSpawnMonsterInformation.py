from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


class BaseSpawnMonsterInformation(SpawnInformation):
    creatureGenericId:int
    

    def init(self, creatureGenericId:int):
        self.creatureGenericId = creatureGenericId
        
        super().__init__()
    
    