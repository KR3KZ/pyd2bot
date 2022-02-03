from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagFurnituresRequestMessage(NetworkMessage):
    cellIds:list[int]
    funitureIds:list[int]
    orientations:list[int]
    

    def init(self, cellIds:list[int], funitureIds:list[int], orientations:list[int]):
        self.cellIds = cellIds
        self.funitureIds = funitureIds
        self.orientations = orientations
        
        super().__init__()
    
    