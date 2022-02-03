from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristicValue(CharacterCharacteristic):
    total:int
    

    def init(self, total:int, characteristicId:int):
        self.total = total
        
        super().__init__(characteristicId)
    
    