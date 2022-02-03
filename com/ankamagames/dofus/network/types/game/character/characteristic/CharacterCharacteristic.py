from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCharacteristic(NetworkMessage):
    characteristicId:int
    

    def init(self, characteristicId:int):
        self.characteristicId = characteristicId
        
        super().__init__()
    
    