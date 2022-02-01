from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop


class ExchangeStartOkNpcShopMessage(NetworkMessage):
    npcSellerId:int
    tokenId:int
    objectsInfos:list[ObjectItemToSellInNpcShop]
    
    
