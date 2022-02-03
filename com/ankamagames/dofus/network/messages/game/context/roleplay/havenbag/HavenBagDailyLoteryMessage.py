from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagDailyLoteryMessage(NetworkMessage):
    returnType:int
    gameActionId:str
    

    def init(self, returnType:int, gameActionId:str):
        self.returnType = returnType
        self.gameActionId = gameActionId
        
        super().__init__()
    
    