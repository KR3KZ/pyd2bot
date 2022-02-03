from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage(NetworkMessage):
    allow:bool
    

    def init(self, allow:bool):
        self.allow = allow
        
        super().__init__()
    
    