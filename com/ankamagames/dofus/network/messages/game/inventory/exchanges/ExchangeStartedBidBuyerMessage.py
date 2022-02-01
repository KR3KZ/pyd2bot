from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor


class ExchangeStartedBidBuyerMessage(INetworkMessage):
    protocolId = 9037
    buyerDescriptor:SellerBuyerDescriptor
    
    
