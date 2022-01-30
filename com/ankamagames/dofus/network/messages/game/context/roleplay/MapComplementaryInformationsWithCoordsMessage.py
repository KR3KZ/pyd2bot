from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsWithCoordsMessage(MapComplementaryInformationsDataMessage):
    protocolId = 5440
    worldX:int
    worldY:int
    
    
