from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentWarEffortInformation(NetworkMessage):
    alignmentSide:int
    alignmentWarEffort:int
    

    def init(self, alignmentSide:int, alignmentWarEffort:int):
        self.alignmentSide = alignmentSide
        self.alignmentWarEffort = alignmentWarEffort
        
        super().__init__()
    
    