
from pyd2bot.game.fight.context.EntityDispositionInformations import EntityDispositionInformations
from pyd2bot.game.fight.context.GameContextActorPositionInformations import GameContextActorPositionInformations
from pyd2bot.game.stats.EntityLook import EntityLook


class GameContextActorInformations(GameContextActorPositionInformations):
   
   
   def __init__(self):
      self.look = EntityLook()
      super().__init__()
   
   def initGameContextActorInformations(self, contextualId:float = 0, disposition:EntityDispositionInformations = None, look:EntityLook = None) -> 'GameContextActorInformations':
      super().initGameContextActorPositionInformations(contextualId, disposition)
      self.look = look
      return self
   
   def reset(self) -> None:
      super().reset()
      self.look = EntityLook()
