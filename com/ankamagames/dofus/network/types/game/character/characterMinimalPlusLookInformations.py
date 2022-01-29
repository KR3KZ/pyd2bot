from com.ankamagames.dofus.network.types.game.character.characterMinimalInformations import CharacterMinimalInformations
from com.ankamagames.dofus.network.types.game.look.entityLook import EntityLook
from com.ankamagames.jerakine.network.iNetworkType import INetworkType


class CharacterMinimalPlusLookInformations(CharacterMinimalInformations, INetworkType):
   
   entityLook:EntityLook
   breed:int = 0
   
   
   def __init__(self):
      self.entityLook = EntityLook()
      super().__init__()
   
   def initCharacterMinimalPlusLookInformations(self, id:float = 0, name:str = "", level:int = 0, entityLook:EntityLook = None, breed:int = 0) -> 'CharacterMinimalPlusLookInformations':
      super().initCharacterMinimalInformations(id,name,level)
      self.entityLook = entityLook
      self.breed = breed
      return self
   
   def reset(self) -> None:
      super().reset()
      self.entityLook = EntityLook()
