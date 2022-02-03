from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachReward import BreachReward
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.MonsterInGroupLightInformations import MonsterInGroupLightInformations
    


class ExtendedBreachBranch(BreachBranch):
    rewards:list['BreachReward']
    modifier:int
    prize:int
    

    def init(self, rewards:list['BreachReward'], modifier:int, prize:int, room:int, element:int, bosses:list['MonsterInGroupLightInformations'], map:int, score:int, relativeScore:int, monsters:list['MonsterInGroupLightInformations']):
        self.rewards = rewards
        self.modifier = modifier
        self.prize = prize
        
        super().__init__(room, element, bosses, map, score, relativeScore, monsters)
    
    