from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination


class TeleportDestinationsMessage(INetworkMessage):
    protocolId = 5651
    type:int
    destinations:TeleportDestination
    
    
