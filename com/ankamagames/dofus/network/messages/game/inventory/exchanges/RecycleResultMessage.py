from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RecycleResultMessage(NetworkMessage):
    nuggetsForPrism:int
    nuggetsForPlayer:int
    

    def init(self, nuggetsForPrism:int, nuggetsForPlayer:int):
        self.nuggetsForPrism = nuggetsForPrism
        self.nuggetsForPlayer = nuggetsForPlayer
        
        super().__init__()
    
    