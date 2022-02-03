from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionFinishedMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    

    def init(self, delayedCharacterId:int, delayTypeId:int):
        self.delayedCharacterId = delayedCharacterId
        self.delayTypeId = delayTypeId
        
        super().__init__()
    
    