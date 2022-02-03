from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SequenceEndMessage(NetworkMessage):
    actionId:int
    authorId:int
    sequenceType:int
    

    def init(self, actionId:int, authorId:int, sequenceType:int):
        self.actionId = actionId
        self.authorId = authorId
        self.sequenceType = sequenceType
        
        super().__init__()
    
    