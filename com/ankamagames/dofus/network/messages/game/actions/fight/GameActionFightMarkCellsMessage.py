from com.ankamagames.dofus.network.messages.game.actions.AbstractGameActionMessage import AbstractGameActionMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMark import GameActionMark
    


class GameActionFightMarkCellsMessage(AbstractGameActionMessage):
    mark:'GameActionMark'
    

    def init(self, mark:'GameActionMark', actionId:int, sourceId:int):
        self.mark = mark
        
        super().__init__(actionId, sourceId)
    
    