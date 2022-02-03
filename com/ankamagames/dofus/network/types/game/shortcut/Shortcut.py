from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class Shortcut(NetworkMessage):
    slot:int
    

    def init(self, slot:int):
        self.slot = slot
        
        super().__init__()
    
    