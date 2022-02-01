from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ObjectModifiedMessage(INetworkMessage):
    protocolId = 2793
    object:ObjectItem
    
    
