from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SpellVariantActivationRequestMessage(NetworkMessage):
    spellId:int
    

    def init(self, spellId:int):
        self.spellId = spellId
        
        super().__init__()
    
    