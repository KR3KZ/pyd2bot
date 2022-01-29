from com.ankamagames.dofus.network.types.game.character.characterBasicMinimalInformations import CharacterBasicMinimalInformations
from com.ankamagames.jerakine.network.iNetworkType import INetworkType


class CharacterMinimalInformations(CharacterBasicMinimalInformations, INetworkType):
   
   level:int = 0
   
   def __init__(self):
      super().__init__()

   def initCharacterMinimalInformations(self, id:float = 0, name:str = "", level:int = 0) -> 'CharacterMinimalInformations':
      super().initCharacterBasicMinimalInformations(id, name)
      self.level = level
      return self
   
   def reset(self) -> None:
      super().reset()
      self.level = 0