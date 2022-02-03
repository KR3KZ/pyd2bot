from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameServerInformations(NetworkMessage):
    id:int
    type:int
    status:int
    completion:int
    charactersCount:int
    charactersSlots:int
    date:int
    isMonoAccount:bool
    isSelectable:bool
    

    def init(self, id:int, type:int, status:int, completion:int, charactersCount:int, charactersSlots:int, date:int):
        self.id = id
        self.type = type
        self.status = status
        self.completion = completion
        self.charactersCount = charactersCount
        self.charactersSlots = charactersSlots
        self.date = date
        
        super().__init__()
    
    