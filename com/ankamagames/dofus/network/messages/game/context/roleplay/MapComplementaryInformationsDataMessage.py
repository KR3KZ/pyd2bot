from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions


class MapComplementaryInformationsDataMessage(NetworkMessage):
    protocolId = 1182
    subAreaId:int
    mapId:int
    houses:HouseInformations
    actors:GameRolePlayActorInformations
    interactiveElements:InteractiveElement
    statedElements:StatedElement
    obstacles:MapObstacle
    fights:FightCommonInformations
    hasAggressiveMonsters:bool
    fightStartPositions:FightStartingPositions
    
