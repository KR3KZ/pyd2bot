from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.CharacterMinimalInformations import CharacterMinimalInformations
    from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.GameRolePlayActorInformations import GameRolePlayActorInformations
    from com.ankamagames.dofus.network.types.game.interactive.InteractiveElement import InteractiveElement
    from com.ankamagames.dofus.network.types.game.interactive.StatedElement import StatedElement
    from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
    from com.ankamagames.dofus.network.types.game.context.fight.FightCommonInformations import FightCommonInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions
    


class MapComplementaryInformationsDataInHavenBagMessage(MapComplementaryInformationsDataMessage):
    ownerInformations:'CharacterMinimalInformations'
    theme:int
    roomId:int
    maxRoomId:int
    

    def init(self, ownerInformations:'CharacterMinimalInformations', theme:int, roomId:int, maxRoomId:int, subAreaId:int, mapId:int, houses:list['HouseInformations'], actors:list['GameRolePlayActorInformations'], interactiveElements:list['InteractiveElement'], statedElements:list['StatedElement'], obstacles:list['MapObstacle'], fights:list['FightCommonInformations'], hasAggressiveMonsters:bool, fightStartPositions:'FightStartingPositions'):
        self.ownerInformations = ownerInformations
        self.theme = theme
        self.roomId = roomId
        self.maxRoomId = maxRoomId
        
        super().__init__(subAreaId, mapId, houses, actors, interactiveElements, statedElements, obstacles, fights, hasAggressiveMonsters, fightStartPositions)
    
    