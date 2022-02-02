from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects


@dataclass
class ExchangeOfflineSoldItemsMessage(NetworkMessage):
    bidHouseItems:list[ObjectItemQuantityPriceDateEffects]
    merchantItems:list[ObjectItemQuantityPriceDateEffects]
    
    
    def __post_init__(self):
        super().__init__()
    