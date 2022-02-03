from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


class SpawnCharacterInformation(SpawnInformation):
    name:str
    level:int
    

    def init(self, name:str, level:int):
        self.name = name
        self.level = level
        
        super().__init__()
    
    