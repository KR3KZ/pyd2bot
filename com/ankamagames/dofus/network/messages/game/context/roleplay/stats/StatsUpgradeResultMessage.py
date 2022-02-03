from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatsUpgradeResultMessage(NetworkMessage):
    result:int
    nbCharacBoost:int
    

    def init(self, result:int, nbCharacBoost:int):
        self.result = result
        self.nbCharacBoost = nbCharacBoost
        
        super().__init__()
    
    