from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage


class ExchangeCraftResultWithObjectIdMessage(ExchangeCraftResultMessage):
    objectGenericId:int
    

    def init(self, objectGenericId:int, craftResult:int):
        self.objectGenericId = objectGenericId
        
        super().__init__(craftResult)
    
    