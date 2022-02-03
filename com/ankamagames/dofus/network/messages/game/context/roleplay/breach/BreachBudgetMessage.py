from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachBudgetMessage(NetworkMessage):
    bugdet:int
    

    def init(self, bugdet:int):
        self.bugdet = bugdet
        
        super().__init__()
    
    