from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceMessage import ExchangeBidPriceMessage


class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
    allIdentical:bool
    minimalPrices:list[int]
    
    
