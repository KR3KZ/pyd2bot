from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceStartMessage(NetworkMessage):
    sequenceType:int
    authorId:int
    

    def init(self, sequenceType:int, authorId:int):
        self.sequenceType = sequenceType
        self.authorId = authorId
        
        super().__init__()
    
    