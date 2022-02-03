from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ItemDurability(NetworkMessage):
    durability:int
    durabilityMax:int
    

    def init(self, durability:int, durabilityMax:int):
        self.durability = durability
        self.durabilityMax = durabilityMax
        
        super().__init__()
    
    