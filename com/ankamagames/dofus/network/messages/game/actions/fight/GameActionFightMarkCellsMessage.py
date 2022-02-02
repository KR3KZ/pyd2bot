from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark


@dataclass
class GameActionFightMarkCellsMessage(AbstractGameActionMessage):
    mark:GameActionMark
    
    
    def __post_init__(self):
        super().__init__()
    