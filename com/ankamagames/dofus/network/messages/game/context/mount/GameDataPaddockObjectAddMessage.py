from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem


class GameDataPaddockObjectAddMessage(NetworkMessage):
    protocolId = 8122
    paddockItemDescription:PaddockItem
    
