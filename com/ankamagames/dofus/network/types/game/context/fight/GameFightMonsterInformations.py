                     
from com.ankamagames.dofus.network.messages.game.context.EntityDispositionInformations import EntityDispositionInformations
from com.ankamagames.dofus.network.types.game.character.characteristic.GameFightCharacteristics import GameFightCharacteristics
from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from com.ankamagames.dofus.network.types.game.context.fight.GameFightAIInformations import GameFightAIInformations
from com.ankamagames.dofus.network.types.game.look.entityLook import EntityLook


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