from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionFightCastOnTargetRequestMessage(NetworkMessage):
    spellId:int
    targetId:int
    

    def init(self, spellId:int, targetId:int):
        self.spellId = spellId
        self.targetId = targetId
        
        super().__init__()
    
    