from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics


class RefreshCharacterStatsMessage(NetworkMessage):
    protocolId = 154
    fighterId:int
    stats:GameFightCharacteristics
    
    
