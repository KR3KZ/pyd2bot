               
class CharacterCharacteristic:
   characteristicId:int = 0
   
   def __init__(self):
      super().__init__()

   def initCharacterCharacteristic(self, characteristicId:int = 0) -> 'CharacterCharacteristic':
      self.characteristicId = characteristicId
      return self
   
   def reset(self) -> None:
      self.characteristicId = 0