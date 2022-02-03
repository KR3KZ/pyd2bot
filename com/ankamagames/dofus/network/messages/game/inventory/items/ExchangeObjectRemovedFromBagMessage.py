from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectRemovedFromBagMessage(ExchangeObjectMessage):
    objectUID:int
    

    def init(self, objectUID:int, remote:bool):
        self.objectUID = objectUID
        
        super().__init__(remote)
    
    