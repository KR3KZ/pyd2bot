from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid


class ExchangeBidHouseItemAddOkMessage(NetworkMessage):
    itemInfo:ObjectItemToSellInBid
    
    
