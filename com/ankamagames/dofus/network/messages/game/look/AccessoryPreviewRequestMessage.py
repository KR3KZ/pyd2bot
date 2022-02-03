from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccessoryPreviewRequestMessage(NetworkMessage):
    genericId:list[int]
    

    def init(self, genericId:list[int]):
        self.genericId = genericId
        
        super().__init__()
    
    