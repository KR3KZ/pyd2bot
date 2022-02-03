from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightFighterLightInformations(NetworkMessage):
    id:int
    wave:int
    level:int
    breed:int
    sex:bool
    alive:bool
    

    def init(self, id:int, wave:int, level:int, breed:int):
        self.id = id
        self.wave = wave
        self.level = level
        self.breed = breed
        
        super().__init__()
    
    