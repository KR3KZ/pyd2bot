from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop


@dataclass
class ExchangeStartOkNpcShopMessage(NetworkMessage):
    npcSellerId:int
    tokenId:int
    objectsInfos:list[ObjectItemToSellInNpcShop]
    
    
    def __post_init__(self):
        super().__init__()
    