from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseInformations(NetworkMessage):
    houseId:int
    modelId:int
    

    def init(self, houseId:int, modelId:int):
        self.houseId = houseId
        self.modelId = modelId
        
        super().__init__()
    
    