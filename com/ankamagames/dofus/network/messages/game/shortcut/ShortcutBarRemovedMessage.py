from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarRemovedMessage(NetworkMessage):
    barType:int
    slot:int
    

    def init(self, barType:int, slot:int):
        self.barType = barType
        self.slot = slot
        
        super().__init__()
    
    