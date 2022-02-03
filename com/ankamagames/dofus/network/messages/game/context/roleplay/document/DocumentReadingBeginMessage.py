from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DocumentReadingBeginMessage(NetworkMessage):
    documentId:int
    

    def init(self, documentId:int):
        self.documentId = documentId
        
        super().__init__()
    
    