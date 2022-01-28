from com.ankamagames.dofus.network.messages.game.context.EntityDispositionInformations import EntityDispositionInformations
from com.ankamagames.dofus.network.types.game.character.characteristic.GameFightCharacteristics import GameFightCharacteristics
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from com.ankamagames.dofus.network.types.game.look.entityLook import EntityLook


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