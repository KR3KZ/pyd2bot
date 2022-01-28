

from pyd2bot.game.fight.context.EntityDispositionInformations import EntityDispositionInformations


class GameContextActorPositionInformations:
   contextualId:float = 0
   disposition:EntityDispositionInformations
   
   def __init__(self):
      self.disposition = EntityDispositionInformations()
   
   def initGameContextActorPositionInformations(self, contextualId:float = 0, disposition:EntityDispositionInformations = None) -> 'GameContextActorPositionInformations':
      self.contextualId = contextualId
      self.disposition = disposition
      return self
   
   def reset(self) -> None:
      self.contextualId = 0
      self.disposition = EntityDispositionInformations()
