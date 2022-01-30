from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid


class ExchangeBidHouseItemAddOkMessage(NetworkMessage):
    protocolId = 7844
    itemInfo:ObjectItemToSellInBid
    
