from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination


class TeleportDestinationsMessage(NetworkMessage):
    type:int
    destinations:list[TeleportDestination]
    
    
