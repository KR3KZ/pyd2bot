from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.BidExchangerObjectInfo import BidExchangerObjectInfo


@dataclass
class ExchangeTypesItemsExchangerDescriptionForUserMessage(NetworkMessage):
    objectType:int
    itemTypeDescriptions:list[BidExchangerObjectInfo]
    
    
    def __post_init__(self):
        super().__init__()
    