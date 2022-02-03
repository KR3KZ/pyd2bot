from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebtsDeleteMessage(NetworkMessage):
    reason:int
    debts:list[int]
    

    def init(self, reason:int, debts:list[int]):
        self.reason = reason
        self.debts = debts
        
        super().__init__()
    
    