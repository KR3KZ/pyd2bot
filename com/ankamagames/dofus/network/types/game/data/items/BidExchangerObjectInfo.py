from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect


class BidExchangerObjectInfo(NetworkMessage):
    protocolId = 461
    objectUID:int
    objectGID:int
    objectType:int
    effects:ObjectEffect
    prices:int
    
    
