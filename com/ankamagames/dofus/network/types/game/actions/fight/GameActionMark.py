from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMarkedCell import GameActionMarkedCell
    


class GameActionMark(NetworkMessage):
    markAuthorId:int
    markTeamId:int
    markSpellId:int
    markSpellLevel:int
    markId:int
    markType:int
    markimpactCell:int
    cells:list['GameActionMarkedCell']
    active:bool
    

    def init(self, markAuthorId:int, markTeamId:int, markSpellId:int, markSpellLevel:int, markId:int, markType:int, markimpactCell:int, cells:list['GameActionMarkedCell'], active:bool):
        self.markAuthorId = markAuthorId
        self.markTeamId = markTeamId
        self.markSpellId = markSpellId
        self.markSpellLevel = markSpellLevel
        self.markId = markId
        self.markType = markType
        self.markimpactCell = markimpactCell
        self.cells = cells
        self.active = active
        
        super().__init__()
    
    