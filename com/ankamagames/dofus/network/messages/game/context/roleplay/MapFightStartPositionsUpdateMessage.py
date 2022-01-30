from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.FightStartingPositions import FightStartingPositions


class MapFightStartPositionsUpdateMessage(NetworkMessage):
    protocolId = 5408
    mapId:int
    fightStartPositions:FightStartingPositions
    
    
