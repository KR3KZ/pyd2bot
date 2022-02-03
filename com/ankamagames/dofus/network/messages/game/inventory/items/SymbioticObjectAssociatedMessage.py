from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SymbioticObjectAssociatedMessage(NetworkMessage):
    hostUID:int
    

    def init(self, hostUID:int):
        self.hostUID = hostUID
        
        super().__init__()
    
    