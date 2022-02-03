from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage(NetworkMessage):
    allowed:bool
    

    def init(self, allowed:bool):
        self.allowed = allowed
        
        super().__init__()
    
    