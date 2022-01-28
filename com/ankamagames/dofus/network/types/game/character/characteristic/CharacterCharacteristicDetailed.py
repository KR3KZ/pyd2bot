from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristicDetailed(CharacterCharacteristic):
   base:int = 0
   additional:int = 0
   objectsAndMountBonus:int = 0
   alignGiftBonus:int = 0
   contextModif:int = 0
   
   def __init__(self):
      super().__init__()
   
   def initCharacterCharacteristicDetailed(self, characteristicId:int = 0, base:int = 0, additional:int = 0, objectsAndMountBonus:int = 0, alignGiftBonus:int = 0, contextModif:int = 0) -> 'CharacterCharacteristicDetailed':
      super().initCharacterCharacteristic(characteristicId)
      self.base = base
      self.additional = additional
      self.objectsAndMountBonus = objectsAndMountBonus
      self.alignGiftBonus = alignGiftBonus
      self.contextModif = contextModif
      return self
   
   def reset(self) -> None:
      super().reset()
      self.base = 0
      self.additional = 0
      self.objectsAndMountBonus = 0
      self.alignGiftBonus = 0
      self.contextModif = 0
