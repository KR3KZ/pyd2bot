from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatsUpgradeRequestMessage(NetworkMessage):
    useAdditionnal:bool
    statId:int
    boostPoint:int
    

    def init(self, useAdditionnal:bool, statId:int, boostPoint:int):
        self.useAdditionnal = useAdditionnal
        self.statId = statId
        self.boostPoint = boostPoint
        
        super().__init__()
    
    