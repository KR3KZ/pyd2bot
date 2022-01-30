from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop


class ExchangeStartOkNpcShopMessage(NetworkMessage):
    protocolId = 8584
    npcSellerId:float
    tokenId:int
    objectsInfos:list[ObjectItemToSellInNpcShop]
    
