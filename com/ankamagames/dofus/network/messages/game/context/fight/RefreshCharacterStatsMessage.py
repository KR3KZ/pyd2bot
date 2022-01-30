from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics


class RefreshCharacterStatsMessage(INetworkMessage):
    protocolId = 154
    fighterId:int
    stats:GameFightCharacteristics
    
    
