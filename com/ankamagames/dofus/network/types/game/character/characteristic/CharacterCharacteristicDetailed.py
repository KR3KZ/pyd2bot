from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristic import CharacterCharacteristic


class CharacterCharacteristicDetailed(CharacterCharacteristic):
    base:int
    additional:int
    objectsAndMountBonus:int
    alignGiftBonus:int
    contextModif:int
    

    def init(self, base:int, additional:int, objectsAndMountBonus:int, alignGiftBonus:int, contextModif:int, characteristicId:int):
        self.base = base
        self.additional = additional
        self.objectsAndMountBonus = objectsAndMountBonus
        self.alignGiftBonus = alignGiftBonus
        self.contextModif = contextModif
        
        super().__init__(characteristicId)
    
    