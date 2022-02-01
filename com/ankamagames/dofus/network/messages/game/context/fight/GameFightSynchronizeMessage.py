from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations


class GameFightSynchronizeMessage(NetworkMessage):
    fighters:list[GameFightFighterInformations]
    
    
