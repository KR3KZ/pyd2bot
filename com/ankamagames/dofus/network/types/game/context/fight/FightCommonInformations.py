from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightTeamInformations import FightTeamInformations
from com.ankamagames.dofus.network.types.game.context.fight.FightOptionsInformations import FightOptionsInformations


@dataclass
class FightCommonInformations(NetworkMessage):
    fightId:int
    fightType:int
    fightTeams:list[FightTeamInformations]
    fightTeamsPositions:list[int]
    fightTeamsOptions:list[FightOptionsInformations]
    
    
    def __post_init__(self):
        super().__init__()
    