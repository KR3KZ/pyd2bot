from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceMessage import ExchangeBidPriceMessage


class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
    protocolId = 8645
    allIdentical:bool
    minimalPrices:list[float]
    
