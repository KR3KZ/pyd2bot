from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    


class BreachBranch(NetworkMessage):
    room:int
    element:int
    bosses:list['MonsterInGroupLightInformations']
    map:int
    score:int
    relativeScore:int
    monsters:list['MonsterInGroupLightInformations']
    

    def init(self, room:int, element:int, bosses:list['MonsterInGroupLightInformations'], map:int, score:int, relativeScore:int, monsters:list['MonsterInGroupLightInformations']):
        self.room = room
        self.element = element
        self.bosses = bosses
        self.map = map
        self.score = score
        self.relativeScore = relativeScore
        self.monsters = monsters
        
        super().__init__()
    
    