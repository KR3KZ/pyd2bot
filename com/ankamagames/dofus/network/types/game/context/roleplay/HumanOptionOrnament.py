from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption


@dataclass
class HumanOptionOrnament(HumanOption):
    ornamentId:int
    level:int
    leagueId:int
    ladderPosition:int
    
    
    def __post_init__(self):
        super().__init__()
    