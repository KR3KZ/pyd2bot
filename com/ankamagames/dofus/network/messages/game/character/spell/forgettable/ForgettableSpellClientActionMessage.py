from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ForgettableSpellClientActionMessage(NetworkMessage):
    spellId:int
    action:int
    

    def init(self, spellId:int, action:int):
        self.spellId = spellId
        self.action = action
        
        super().__init__()
    
    