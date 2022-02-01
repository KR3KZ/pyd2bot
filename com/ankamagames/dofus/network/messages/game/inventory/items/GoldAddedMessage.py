from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.GoldItem import GoldItem


class GoldAddedMessage(INetworkMessage):
    protocolId = 1408
    gold:GoldItem
    
    
