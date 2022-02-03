from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionSpamMessage(NetworkMessage):
    cells:list[int]
    

    def init(self, cells:list[int]):
        self.cells = cells
        
        super().__init__()
    
    