from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectTransfertListWithQuantityToInvMessage(NetworkMessage):
    ids:list[int]
    qtys:list[int]
    

    def init(self, ids:list[int], qtys:list[int]):
        self.ids = ids
        self.qtys = qtys
        
        super().__init__()
    
    