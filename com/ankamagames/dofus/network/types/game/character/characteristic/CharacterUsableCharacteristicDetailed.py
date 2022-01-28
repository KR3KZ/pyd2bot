from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed

class CharacterUsableCharacteristicDetailed(CharacterCharacteristicDetailed):
   
   def __init__(self):
      super().__init__()
      self.used:int = 0
   
   def initCharacterUsableCharacteristicDetailed(self, characteristicId:int = 0, base:int = 0, additional:int = 0, objectsAndMountBonus:int = 0, alignGiftBonus:int = 0, contextModif:int = 0, used:int = 0) -> 'CharacterUsableCharacteristicDetailed':
      super().initCharacterCharacteristicDetailed(
         characteristicId,
         base,
         additional,
         objectsAndMountBonus,
         alignGiftBonus,
         contextModif
      )
      self.used = used
      return self
   
   def reset(self) -> None:
      super().reset()
      self.used = 0
