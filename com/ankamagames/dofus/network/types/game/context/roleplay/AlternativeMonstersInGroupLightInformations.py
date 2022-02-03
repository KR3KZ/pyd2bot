from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    


class AlternativeMonstersInGroupLightInformations(NetworkMessage):
    playerCount:int
    monsters:list['MonsterInGroupLightInformations']
    

    def init(self, playerCount:int, monsters:list['MonsterInGroupLightInformations']):
        self.playerCount = playerCount
        self.monsters = monsters
        
        super().__init__()
    
    