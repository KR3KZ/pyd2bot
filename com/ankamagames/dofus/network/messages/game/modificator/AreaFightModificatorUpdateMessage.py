from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AreaFightModificatorUpdateMessage(NetworkMessage):
    spellPairId:int
    

    def init(self, spellPairId:int):
        self.spellPairId = spellPairId
        
        super().__init__()
    
    