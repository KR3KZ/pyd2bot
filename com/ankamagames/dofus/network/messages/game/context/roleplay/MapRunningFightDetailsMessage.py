from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterLightInformations import GameFightFighterLightInformations


@dataclass
class MapRunningFightDetailsMessage(NetworkMessage):
    fightId:int
    attackers:list[GameFightFighterLightInformations]
    defenders:list[GameFightFighterLightInformations]
    
    
    def __post_init__(self):
        super().__init__()
    