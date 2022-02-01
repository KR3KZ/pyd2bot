from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions


class MapFightStartPositionsUpdateMessage(INetworkMessage):
    protocolId = 5408
    mapId:int
    fightStartPositions:FightStartingPositions
    
    
