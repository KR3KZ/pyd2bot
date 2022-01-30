from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class ExchangeBidHouseInListAddedMessage(INetworkMessage):
    protocolId = 213
    itemUID:int
    objectGID:int
    objectType:int
    effects:ObjectEffect
    prices:int
    
    
