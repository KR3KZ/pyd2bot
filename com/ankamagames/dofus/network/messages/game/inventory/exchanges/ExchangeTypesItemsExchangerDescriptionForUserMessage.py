from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.BidExchangerObjectInfo import BidExchangerObjectInfo


class ExchangeTypesItemsExchangerDescriptionForUserMessage(NetworkMessage):
    protocolId = 6681
    objectType:int
    itemTypeDescriptions:BidExchangerObjectInfo
    
