

from com.ankamagames.dofus.network.messages.game.context.EntityDispositionInformations import EntityDispositionInformations
from com.ankamagames.dofus.network.types.game.context.GameContextActorPositionInformations import GameContextActorPositionInformations
from com.ankamagames.dofus.network.types.game.look.entityLook import EntityLook

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
