from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.BidExchangerObjectInfo import BidExchangerObjectInfo


class ExchangeTypesItemsExchangerDescriptionForUserMessage(NetworkMessage):
    objectType:int
    itemTypeDescriptions:list[BidExchangerObjectInfo]
    
    
