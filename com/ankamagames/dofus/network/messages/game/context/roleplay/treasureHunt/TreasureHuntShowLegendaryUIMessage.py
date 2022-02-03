from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntShowLegendaryUIMessage(NetworkMessage):
    availableLegendaryIds:list[int]
    

    def init(self, availableLegendaryIds:list[int]):
        self.availableLegendaryIds = availableLegendaryIds
        
        super().__init__()
    
    