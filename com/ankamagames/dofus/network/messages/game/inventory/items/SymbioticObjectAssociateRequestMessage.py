from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SymbioticObjectAssociateRequestMessage(NetworkMessage):
    symbioteUID:int
    symbiotePos:int
    hostUID:int
    hostPos:int
    

    def init(self, symbioteUID:int, symbiotePos:int, hostUID:int, hostPos:int):
        self.symbioteUID = symbioteUID
        self.symbiotePos = symbiotePos
        self.hostUID = hostUID
        self.hostPos = hostPos
        
        super().__init__()
    
    