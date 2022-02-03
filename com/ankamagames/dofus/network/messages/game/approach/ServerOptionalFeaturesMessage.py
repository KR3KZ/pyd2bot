from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ServerOptionalFeaturesMessage(NetworkMessage):
    features:list[int]
    

    def init(self, features:list[int]):
        self.features = features
        
        super().__init__()
    
    