from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMarkedCell import GameActionMarkedCell


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
    
    
