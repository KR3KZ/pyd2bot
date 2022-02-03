from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnListMessage(NetworkMessage):
    ids:list[int]
    deadsIds:list[int]
    

    def init(self, ids:list[int], deadsIds:list[int]):
        self.ids = ids
        self.deadsIds = deadsIds
        
        super().__init__()
    
    