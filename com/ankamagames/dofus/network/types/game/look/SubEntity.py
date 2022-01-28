               


from com.ankamagames.dofus.network.messages.types.game.look import EntityLook


class SubEntity:
   bindingPointCategory:int = 0
   bindingPointIndex:int = 0
   subEntityLook:EntityLook
   
   def __init__(self):
      self.subEntityLook = EntityLook()
      super().__init__()
   
   def getTypeId(self) -> int:
      return 8670
   
   def initSubEntity(self, bindingPointCategory:int = 0, bindingPointIndex:int = 0, subEntityLook:EntityLook = None) -> 'SubEntity':
      self.bindingPointCategory = bindingPointCategory
      self.bindingPointIndex = bindingPointIndex
      self.subEntityLook = subEntityLook
      return self
   
   def reset(self) -> None:
      self.bindingPointCategory = 0
      self.bindingPointIndex = 0
      self.subEntityLook = EntityLook()