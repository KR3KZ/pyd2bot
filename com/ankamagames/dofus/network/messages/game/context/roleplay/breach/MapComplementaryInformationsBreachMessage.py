from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch


class MapComplementaryInformationsBreachMessage(MapComplementaryInformationsDataMessage):
    floor:int
    room:int
    infinityMode:int
    branches:list[BreachBranch]
    
    
