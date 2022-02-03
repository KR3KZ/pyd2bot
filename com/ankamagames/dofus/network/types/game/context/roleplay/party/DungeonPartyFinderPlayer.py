from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DungeonPartyFinderPlayer(NetworkMessage):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    

    def init(self, playerId:int, playerName:str, breed:int, sex:bool, level:int):
        self.playerId = playerId
        self.playerName = playerName
        self.breed = breed
        self.sex = sex
        self.level = level
        
        super().__init__()
    
    