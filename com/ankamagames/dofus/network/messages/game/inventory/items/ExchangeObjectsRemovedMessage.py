from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectsRemovedMessage(ExchangeObjectMessage):
    objectUID:list[int]
    

    def init(self, objectUID:list[int], remote:bool):
        self.objectUID = objectUID
        
        super().__init__(remote)
    
    