from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMarkedCell import GameActionMarkedCell


class GameActionMark(NetworkMessage):
    protocolId = 158
    markAuthorId:float
    markTeamId:int
    markSpellId:int
    markSpellLevel:int
    markId:int
    markType:int
    markimpactCell:int
    cells:list[GameActionMarkedCell]
    active:bool
    
