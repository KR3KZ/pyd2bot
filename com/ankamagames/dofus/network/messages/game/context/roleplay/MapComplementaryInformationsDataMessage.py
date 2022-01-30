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
    mapId:float
    houses:list[HouseInformations]
    actors:list[GameRolePlayActorInformations]
    interactiveElements:list[InteractiveElement]
    statedElements:list[StatedElement]
    obstacles:list[MapObstacle]
    fights:list[FightCommonInformations]
    hasAggressiveMonsters:bool
    fightStartPositions:FightStartingPositions
    
