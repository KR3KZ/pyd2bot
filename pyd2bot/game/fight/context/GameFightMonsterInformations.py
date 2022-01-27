                     
from pyd2bot.game.fight.characteristic.GameFightCharacteristics import GameFightCharacteristics
from pyd2bot.game.fight.context.EntityDispositionInformations import EntityDispositionInformations
from pyd2bot.game.fight.context.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from pyd2bot.game.fight.context.GameFightAIInformations import GameFightAIInformations
from pyd2bot.game.stats.EntityLook import EntityLook


class GameFightMonsterInformations(GameFightAIInformations):
   creatureGenericId:int = 0
   creatureGrade:int = 0
   creatureLevel:int = 0
   
   def __init__(self):
      super().__init__()
   
   def initGameFightMonsterInformations(
      self, 
      contextualId:float = 0, 
      disposition:EntityDispositionInformations = None, 
      look:EntityLook = None,
      spawnInfo:GameContextBasicSpawnInformation = None, 
      wave:int = 0, 
      stats:GameFightCharacteristics = None, 
      previousPositions:list[int] = None, 
      creatureGenericId:int = 0, 
      creatureGrade:int = 0, 
      creatureLevel:int = 0
   ) -> 'GameFightMonsterInformations':
      super().initGameFightAIInformations(contextualId,disposition,look,spawnInfo,wave,stats,previousPositions)
      self.creatureGenericId = creatureGenericId
      self.creatureGrade = creatureGrade
      self.creatureLevel = creatureLevel
      return self
   
   def reset(self) -> None:
      super().reset()
      self.creatureGenericId = 0
      self.creatureGrade = 0
      self.creatureLevel = 0