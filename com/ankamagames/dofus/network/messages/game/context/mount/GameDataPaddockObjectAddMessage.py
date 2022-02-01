from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem


class GameDataPaddockObjectAddMessage(NetworkMessage):
    paddockItemDescription:PaddockItem
    
    
