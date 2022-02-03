from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class BreachCharactersMessage(NetworkMessage):
    characters:list[int]
    

    def init(self, characters:list[int]):
        self.characters = characters
        
        super().__init__()
    
    