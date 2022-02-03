from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightEffectTriggerCount(NetworkMessage):
    effectId:int
    targetId:int
    count:int
    

    def init(self, effectId:int, targetId:int, count:int):
        self.effectId = effectId
        self.targetId = targetId
        self.count = count
        
        super().__init__()
    
    