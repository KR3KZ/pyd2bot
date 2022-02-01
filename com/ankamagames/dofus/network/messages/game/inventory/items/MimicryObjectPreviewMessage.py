from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class MimicryObjectPreviewMessage(INetworkMessage):
    protocolId = 1198
    result:ObjectItem
    
    
