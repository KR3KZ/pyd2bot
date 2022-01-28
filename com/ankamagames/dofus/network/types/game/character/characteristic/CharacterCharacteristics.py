from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic
from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


class CharacterCharacteristics:
   characteristics:list[CharacterCharacteristicDetailed]

   def __init__(self):
      self.characteristics = list[CharacterCharacteristic]()
   
   def initCharacterCharacteristics(self, characteristics:list[CharacterCharacteristic] = None) -> 'CharacterCharacteristics':
      self.characteristics = characteristics
      return self
   
   def reset(self) -> None:
      self.characteristics = list[CharacterCharacteristic]()
