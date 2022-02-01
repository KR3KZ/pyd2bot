from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics


class RefreshCharacterStatsMessage(NetworkMessage):
    fighterId:int
    stats:GameFightCharacteristics
    
    
