from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultListEntry(NetworkMessage):
    outcome:int
    wave:int
    rewards:'FightLoot'
    

    def init(self, outcome:int, wave:int, rewards:'FightLoot'):
        self.outcome = outcome
        self.wave = wave
        self.rewards = rewards
        
        super().__init__()
    
    