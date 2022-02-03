from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundListAddedMessage(NetworkMessage):
    cells:list[int]
    referenceIds:list[int]
    

    def init(self, cells:list[int], referenceIds:list[int]):
        self.cells = cells
        self.referenceIds = referenceIds
        
        super().__init__()
    
    