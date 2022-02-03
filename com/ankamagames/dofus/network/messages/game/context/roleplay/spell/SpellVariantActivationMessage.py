from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellVariantActivationMessage(NetworkMessage):
    spellId:int
    result:bool
    

    def init(self, spellId:int, result:bool):
        self.spellId = spellId
        self.result = result
        
        super().__init__()
    
    