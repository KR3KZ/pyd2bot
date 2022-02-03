from com.ankamagames.dofus.network.types.game.context.roleplay.breach.ExtendedBreachBranch import ExtendedBreachBranch
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    


class ExtendedLockedBreachBranch(ExtendedBreachBranch):
    unlockPrice:int
    

    def init(self, unlockPrice:int, rewards:list['BreachReward'], modifier:int, prize:int, room:int, element:int, bosses:list['MonsterInGroupLightInformations'], map:int, score:int, relativeScore:int, monsters:list['MonsterInGroupLightInformations']):
        self.unlockPrice = unlockPrice
        
        super().__init__(rewards, modifier, prize, room, element, bosses, map, score, relativeScore, monsters)
    
    