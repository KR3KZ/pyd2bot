from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismUseRequestMessage(NetworkMessage):
    moduleToUse:int
    

    def init(self, moduleToUse:int):
        self.moduleToUse = moduleToUse
        
        super().__init__()
    
    