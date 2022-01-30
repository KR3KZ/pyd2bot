from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop


class ExchangeStartOkNpcShopMessage(NetworkMessage):
    protocolId = 8584
    npcSellerId:int
    tokenId:int
    objectsInfos:ObjectItemToSellInNpcShop
    
    
