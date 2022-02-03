from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMessage(NetworkMessage):
    cell:int
    

    def init(self, cell:int):
        self.cell = cell
        
        super().__init__()
    
    