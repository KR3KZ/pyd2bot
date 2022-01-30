from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch


class MapComplementaryInformationsBreachMessage(MapComplementaryInformationsDataMessage):
    protocolId = 6429
    floor:int
    room:int
    infinityMode:int
    branches:list[BreachBranch]
    
