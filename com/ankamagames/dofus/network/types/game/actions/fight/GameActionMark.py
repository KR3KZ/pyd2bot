from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.actions.fight.GameActionMarkedCell import GameActionMarkedCell


class GameActionMark(INetworkMessage):
    protocolId = 158
    markAuthorId:int
    markTeamId:int
    markSpellId:int
    markSpellLevel:int
    markId:int
    markType:int
    markimpactCell:int
    cells:GameActionMarkedCell
    active:bool
    
    
