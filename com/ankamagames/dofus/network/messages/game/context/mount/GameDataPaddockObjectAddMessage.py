from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.paddock.PaddockItem import PaddockItem


class GameDataPaddockObjectAddMessage(INetworkMessage):
    protocolId = 8122
    paddockItemDescription:PaddockItem
    
    
