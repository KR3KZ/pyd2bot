from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem


class GameDataPaddockObjectListAddMessage(INetworkMessage):
    protocolId = 6584
    paddockItemDescription:PaddockItem
    
    
