from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.GoldItem import GoldItem


class GoldAddedMessage(NetworkMessage):
    protocolId = 1408
    gold:GoldItem
    
    
