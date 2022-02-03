from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FightLoot(NetworkMessage):
    objects:list[int]
    kamas:int
    

    def init(self, objects:list[int], kamas:int):
        self.objects = objects
        self.kamas = kamas
        
        super().__init__()
    
    