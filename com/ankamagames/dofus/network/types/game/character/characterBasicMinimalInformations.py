from com.ankamagames.dofus.network.types.game.character.abstractCharacterInformation import AbstractCharacterInformation
from com.ankamagames.jerakine.network.iNetworkType import INetworkType


class CharacterBasicMinimalInformations(AbstractCharacterInformation, INetworkType):
   
   name:str = ""
   
   def __init__(self):
      super().__init__()
   
   def initCharacterBasicMinimalInformations(self, id:float = 0, name:str = "") -> 'CharacterBasicMinimalInformations':
      super().initAbstractCharacterInformation(id)
      self.name = name
      return self
   
   def reset(self) -> None:
      super().reset()
      self.name = ""