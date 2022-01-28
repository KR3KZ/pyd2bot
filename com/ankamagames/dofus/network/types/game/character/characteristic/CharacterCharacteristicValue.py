               
from pyd2bot.game.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristicValue(CharacterCharacteristic):

   total:int = 0
   def __init__(self):
      super().__init__()

   def initCharacterCharacteristicValue(self, characteristicId:int = 0, total:int = 0) -> 'CharacterCharacteristicValue':
      super().initCharacterCharacteristic(characteristicId)
      self.total = total
      return self
   
   def reset(self) -> None:
      super().reset()
      self.total = 0