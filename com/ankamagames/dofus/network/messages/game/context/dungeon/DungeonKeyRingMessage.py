from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonKeyRingMessage(NetworkMessage):
    availables:list[int]
    unavailables:list[int]
    

    def init(self, availables:list[int], unavailables:list[int]):
        self.availables = availables
        self.unavailables = unavailables
        
        super().__init__()
    
    