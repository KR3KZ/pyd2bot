from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterDeletionRequestMessage(NetworkMessage):
    characterId:int
    secretAnswerHash:str
    

    def init(self, characterId:int, secretAnswerHash:str):
        self.characterId = characterId
        self.secretAnswerHash = secretAnswerHash
        
        super().__init__()
    
    