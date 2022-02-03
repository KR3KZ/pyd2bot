from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightStateUpdateMessage(NetworkMessage):
    state:int
    

    def init(self, state:int):
        self.state = state
        
        super().__init__()
    
    