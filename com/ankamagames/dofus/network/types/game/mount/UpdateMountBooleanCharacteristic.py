from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


class UpdateMountBooleanCharacteristic(UpdateMountCharacteristic):
    value:bool
    

    def init(self, value:bool, type:int):
        self.value = value
        
        super().__init__(type)
    
    