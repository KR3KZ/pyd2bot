from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellDeleteMessage(NetworkMessage):
    reason:int
    spells:list[int]
    

    def init(self, reason:int, spells:list[int]):
        self.reason = reason
        self.spells = spells
        
        super().__init__()
    
    