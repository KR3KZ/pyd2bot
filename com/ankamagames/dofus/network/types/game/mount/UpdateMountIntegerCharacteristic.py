from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


class UpdateMountIntegerCharacteristic(UpdateMountCharacteristic):
    value:int
    

    def init(self, value:int, type:int):
        self.value = value
        
        super().__init__(type)
    
    