from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SlaveNoLongerControledMessage(NetworkMessage):
    masterId:int
    slaveId:int
    

    def init(self, masterId:int, slaveId:int):
        self.masterId = masterId
        self.slaveId = slaveId
        
        super().__init__()
    
    