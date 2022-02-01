from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions


class MapFightStartPositionsUpdateMessage(NetworkMessage):
    mapId:int
    fightStartPositions:FightStartingPositions
    
    
