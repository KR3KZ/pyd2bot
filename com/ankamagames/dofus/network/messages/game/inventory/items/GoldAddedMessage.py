from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.GoldItem import GoldItem


class GoldAddedMessage(NetworkMessage):
    gold:GoldItem
    
    
