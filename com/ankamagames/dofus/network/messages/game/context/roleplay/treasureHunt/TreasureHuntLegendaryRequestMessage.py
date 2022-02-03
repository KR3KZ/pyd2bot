from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntLegendaryRequestMessage(NetworkMessage):
    legendaryId:int
    

    def init(self, legendaryId:int):
        self.legendaryId = legendaryId
        
        super().__init__()
    
    