from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ObjectAddedMessage(INetworkMessage):
    protocolId = 9659
    object:ObjectItem
    origin:int
    
    
