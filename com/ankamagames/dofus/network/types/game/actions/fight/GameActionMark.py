from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMarkedCell import GameActionMarkedCell


@dataclass
class GameActionMark(NetworkMessage):
    markAuthorId:int
    markTeamId:int
    markSpellId:int
    markSpellLevel:int
    markId:int
    markType:int
    markimpactCell:int
    cells:list[GameActionMarkedCell]
    active:bool
    
    
    def __post_init__(self):
        super().__init__()
    