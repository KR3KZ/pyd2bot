from pyd2bot.game.fight.characteristic.GameFightCharacteristics import GameFightCharacteristics
from pyd2bot.game.fight.context.EntityDispositionInformations import EntityDispositionInformations
from pyd2bot.game.fight.context.GameContextActorInformations import GameContextActorInformations
from pyd2bot.game.fight.context.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from pyd2bot.game.stats.EntityLook import EntityLook


class GameFightFighterInformations(GameContextActorInformations):
   
   spawnInfo:GameContextBasicSpawnInformation
   wave:int = 0
   stats:GameFightCharacteristics
   previousPositions:list[int]
   
   def __init__(self):
      self.spawnInfo = GameContextBasicSpawnInformation()
      self.stats = GameFightCharacteristics()
      self.previousPositions = list[int]()
      super().__init__()
   
   def initGameFightFighterInformations(
      self,
      contextualId:float = 0,
      disposition:EntityDispositionInformations = None,
      look:EntityLook = None,
      spawnInfo:GameContextBasicSpawnInformation = None,
      wave:int = 0,
      stats:GameFightCharacteristics = None,
      previousPositions:list[int] = None) -> 'GameFightFighterInformations':

      super().initGameContextActorInformations(contextualId, disposition, look)
      self.spawnInfo = spawnInfo
      self.wave = wave
      self.stats = stats
      self.previousPositions = previousPositions
      return self
   
   def reset(self) -> None:
      super().reset()
      self.spawnInfo = GameContextBasicSpawnInformation()
      self.stats = GameFightCharacteristics()