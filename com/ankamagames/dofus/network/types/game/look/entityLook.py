from pyd2bot.game.stats.SubEntity import SubEntity


class EntityLook:

   bonesId:int = 0
   skins:list[int]
   indexedColors:list[int]
   scales:list[int]
   subentities:list[SubEntity]
   
   def __init__(self):
      self.skins = list[int]()
      self.indexedColors = list[int]()
      self.scales = list[int]()
      self.subentities = list[SubEntity]()
      super().__init__()
   
   def getTypeId(self) -> int:
      return 9546
   
   def initEntityLook(self, bonesId:int = 0, skins:list[int] = None, indexedColors:list[int] = None, scales:list[int] = None, subentities:list[SubEntity] = None) -> 'EntityLook':
      self.bonesId = bonesId
      self.skins = skins
      self.indexedColors = indexedColors
      self.scales = scales
      self.subentities = subentities
      return self
   
   def reset(self) -> None:
      self.bonesId = 0
      self.skins = list[int]()
      self.indexedColors = list[int]()
      self.scales = list[int]()
      self.subentities = list[SubEntity]()
   