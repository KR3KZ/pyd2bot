from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableStateUpdateAbstractMessage(NetworkMessage):
    locked:bool
    

    def init(self, locked:bool):
        self.locked = locked
        
        super().__init__()
    
    