from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor


class ExchangeStartedBidBuyerMessage(NetworkMessage):
    protocolId = 9037
    buyerDescriptor:SellerBuyerDescriptor
    
