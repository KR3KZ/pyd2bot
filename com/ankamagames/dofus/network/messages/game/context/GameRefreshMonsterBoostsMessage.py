from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts


class GameRefreshMonsterBoostsMessage(INetworkMessage):
    protocolId = 2110
    monsterBoosts:MonsterBoosts
    familyBoosts:MonsterBoosts
    
    
