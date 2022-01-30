from com.ankamagames.dofus.network.messages.game.interactive.zaap.TeleportDestinationsMessage import TeleportDestinationsMessage


class ZaapDestinationsMessage(TeleportDestinationsMessage):
    protocolId = 4167
    spawnMapId:float
    
