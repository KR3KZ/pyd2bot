from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop


class ExchangeStartOkNpcShopMessage(INetworkMessage):
    protocolId = 8584
    npcSellerId:int
    tokenId:int
    objectsInfos:ObjectItemToSellInNpcShop
    
    
