from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterBoosts import MonsterBoosts
    


class GameRefreshMonsterBoostsMessage(NetworkMessage):
    monsterBoosts:list['MonsterBoosts']
    familyBoosts:list['MonsterBoosts']
    

    def init(self, monsterBoosts:list['MonsterBoosts'], familyBoosts:list['MonsterBoosts']):
        self.monsterBoosts = monsterBoosts
        self.familyBoosts = familyBoosts
        
        super().__init__()
    
    