

from com.ankamagames.dofus.network.messages.game.context.EntityDispositionInformations import EntityDispositionInformations
from com.ankamagames.dofus.network.types.game.character.characteristic.GameFightCharacteristics import GameFightCharacteristics
from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from com.ankamagames.dofus.network.types.game.look.entityLook import EntityLook


class GameFightAIInformations(GameFightFighterInformations):
   
   def __init__(self):
      super().__init__()
   
   def initGameFightAIInformations(
      self, 
      contextualId:float = 0, 
      disposition:EntityDispositionInformations = None, 
      look:EntityLook = None, 
      spawnInfo:GameContextBasicSpawnInformation = None, 
      wave:int = 0, 
      stats:GameFightCharacteristics = None, 
      previousPositions:list[int] = None
   ) -> 'GameFightAIInformations':
      super().initGameFightFighterInformations(contextualId,disposition,look,spawnInfo,wave,stats,previousPositions)
      return self
   
   def reset(self) -> None:
      super().reset()