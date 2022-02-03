from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StartupActionsObjetAttributionMessage(NetworkMessage):
    actionId:int
    characterId:int
    

    def init(self, actionId:int, characterId:int):
        self.actionId = actionId
        self.characterId = characterId
        
        super().__init__()
    
    