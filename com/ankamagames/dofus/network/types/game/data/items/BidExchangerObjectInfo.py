from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class BidExchangerObjectInfo(INetworkMessage):
    protocolId = 461
    objectUID:int
    objectGID:int
    objectType:int
    effects:ObjectEffect
    prices:int
    
    
