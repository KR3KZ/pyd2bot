                  
from pyd2bot.game.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristics:
   characteristics:list[CharacterCharacteristic]

   def __init__(self):
      self.characteristics = list[CharacterCharacteristic]()
   
   def initCharacterCharacteristics(self, characteristics:list[CharacterCharacteristic] = None) -> 'CharacterCharacteristics':
      self.characteristics = characteristics
      return self
   
   def reset(self) -> None:
      self.characteristics = list[CharacterCharacteristic]()
