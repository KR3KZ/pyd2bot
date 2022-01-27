

from pyd2bot.game.fight.context.EntityDispositionInformations import EntityDispositionInformations


class FightEntityDispositionInformations(EntityDispositionInformations):
   carryingCharacterId:float = 0
   
   def __init__(self):
      super().__init__()
   
   def initFightEntityDispositionInformations(self, cellId:int = 0, direction:int = 1, carryingCharacterId:float = 0) -> 'FightEntityDispositionInformations':
      super().initEntityDispositionInformations(cellId, direction)
      self.carryingCharacterId = carryingCharacterId
      return self
   
   def reset(self) -> None:
      super().reset()
      self.carryingCharacterId = 0