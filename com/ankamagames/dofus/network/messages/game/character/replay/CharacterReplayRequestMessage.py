from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterReplayRequestMessage(NetworkMessage):
    characterId:int
    

    def init(self, characterId:int):
        self.characterId = characterId
        
        super().__init__()
    
    