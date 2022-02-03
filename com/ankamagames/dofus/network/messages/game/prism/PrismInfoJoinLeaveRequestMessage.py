from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismInfoJoinLeaveRequestMessage(NetworkMessage):
    join:bool
    

    def init(self, join:bool):
        self.join = join
        
        super().__init__()
    
    