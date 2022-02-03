from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterNameSuggestionSuccessMessage(NetworkMessage):
    suggestion:str
    

    def init(self, suggestion:str):
        self.suggestion = suggestion
        
        super().__init__()
    
    