from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceMessage import ExchangeBidPriceMessage


class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
    allIdentical:bool
    minimalPrices:list[int]
    

    def init(self, allIdentical:bool, minimalPrices:list[int], genericId:int, averagePrice:int):
        self.allIdentical = allIdentical
        self.minimalPrices = minimalPrices
        
        super().__init__(genericId, averagePrice)
    
    