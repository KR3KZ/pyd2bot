from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountInformationsForPaddock(NetworkMessage):
    modelId:int
    name:str
    ownerName:str
    

    def init(self, modelId:int, name:str, ownerName:str):
        self.modelId = modelId
        self.name = name
        self.ownerName = ownerName
        
        super().__init__()
    
    