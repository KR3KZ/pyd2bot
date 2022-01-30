from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.BidExchangerObjectInfo import BidExchangerObjectInfo


class ExchangeTypesItemsExchangerDescriptionForUserMessage(INetworkMessage):
    protocolId = 6681
    objectType:int
    itemTypeDescriptions:BidExchangerObjectInfo
    
    
