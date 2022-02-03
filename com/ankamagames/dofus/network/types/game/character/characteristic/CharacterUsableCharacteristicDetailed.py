from com.ankamagames.dofus.network.types.game.character.characteristic.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed


class CharacterUsableCharacteristicDetailed(CharacterCharacteristicDetailed):
    used:int
    

    def init(self, used:int, base:int, additional:int, objectsAndMountBonus:int, alignGiftBonus:int, contextModif:int, characteristicId:int):
        self.used = used
        
        super().__init__(base, additional, objectsAndMountBonus, alignGiftBonus, contextModif, characteristicId)
    
    