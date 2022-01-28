                     
from pyd2bot.game.fight.characteristic.GameFightCharacteristics import GameFightCharacteristics
from pyd2bot.game.fight.context.EntityDispositionInformations import EntityDispositionInformations
from pyd2bot.game.fight.context.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from pyd2bot.game.fight.context.GameFightFighterInformations import GameFightFighterInformations
from com.ankamagames.dofus.network.messages.types.game.look import EntityLook


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