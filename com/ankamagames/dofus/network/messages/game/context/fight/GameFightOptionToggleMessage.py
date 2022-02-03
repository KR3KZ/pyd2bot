from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightOptionToggleMessage(NetworkMessage):
    option:int
    

    def init(self, option:int):
        self.option = option
        
        super().__init__()
    
    