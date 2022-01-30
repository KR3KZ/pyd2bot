from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsAnomalyMessage(MapComplementaryInformationsDataMessage):
    protocolId = 6414
    level:int
    closingTime:float
    
