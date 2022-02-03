from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShortcutBarSwapRequestMessage(NetworkMessage):
    barType:int
    firstSlot:int
    secondSlot:int
    

    def init(self, barType:int, firstSlot:int, secondSlot:int):
        self.barType = barType
        self.firstSlot = firstSlot
        self.secondSlot = secondSlot
        
        super().__init__()
    
    