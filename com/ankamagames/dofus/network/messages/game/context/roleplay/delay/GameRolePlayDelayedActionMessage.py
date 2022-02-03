from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayDelayedActionMessage(NetworkMessage):
    delayedCharacterId:int
    delayTypeId:int
    delayEndTime:int
    

    def init(self, delayedCharacterId:int, delayTypeId:int, delayEndTime:int):
        self.delayedCharacterId = delayedCharacterId
        self.delayTypeId = delayTypeId
        self.delayEndTime = delayEndTime
        
        super().__init__()
    
    