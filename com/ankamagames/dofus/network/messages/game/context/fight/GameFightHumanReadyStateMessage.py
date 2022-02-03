from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightHumanReadyStateMessage(NetworkMessage):
    characterId:int
    isReady:bool
    

    def init(self, characterId:int, isReady:bool):
        self.characterId = characterId
        self.isReady = isReady
        
        super().__init__()
    
    