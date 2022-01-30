from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination


class TeleportDestinationsMessage(NetworkMessage):
    protocolId = 5651
    type:int
    destinations:list[TeleportDestination]
    
