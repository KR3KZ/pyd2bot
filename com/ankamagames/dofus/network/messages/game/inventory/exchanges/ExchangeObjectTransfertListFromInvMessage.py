from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListFromInvMessage(NetworkMessage):
    ids:list[int]
    

    def init(self, ids:list[int]):
        self.ids = ids
        
        super().__init__()
    
    