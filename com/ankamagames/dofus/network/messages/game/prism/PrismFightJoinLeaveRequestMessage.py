from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightJoinLeaveRequestMessage(NetworkMessage):
    subAreaId:int
    join:bool
    

    def init(self, subAreaId:int, join:bool):
        self.subAreaId = subAreaId
        self.join = join
        
        super().__init__()
    
    