from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CinematicMessage(NetworkMessage):
    cinematicId:int
    

    def init(self, cinematicId:int):
        self.cinematicId = cinematicId
        
        super().__init__()
    
    