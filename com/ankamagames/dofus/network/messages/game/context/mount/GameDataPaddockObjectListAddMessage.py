from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem


class GameDataPaddockObjectListAddMessage(NetworkMessage):
    protocolId = 6584
    paddockItemDescription:PaddockItem
    
    
