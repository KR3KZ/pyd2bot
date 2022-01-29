from com.ankamagames.dofus.network.types.game.character.characterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from com.ankamagames.dofus.network.types.game.look.entityLook import EntityLook
from com.ankamagames.jerakine.network.iNetworkType import INetworkType


class CharacterBaseInformations(CharacterMinimalPlusLookInformations, INetworkType):
   
   protocolId:int = 8097
      
   
   sex:bool = False
   
   def __init__(self):
      super().__init__()
   
   def getTypeId(self) -> int:
      return 8097
   
   def initCharacterBaseInformations(self, id:float = 0, name:str = "", level:int = 0, entityLook:EntityLook = None, breed:int = 0, sex:bool = False) -> 'CharacterBaseInformations':
      super().initCharacterMinimalPlusLookInformations(id,name,level,entityLook,breed)
      self.sex = sex
      return self
   
   def reset(self) -> None:
      super().reset()
      self.sex = False
   
   