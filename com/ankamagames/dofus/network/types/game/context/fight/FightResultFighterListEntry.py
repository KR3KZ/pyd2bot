from com.ankamagames.dofus.network.types.game.context.fight.FightResultListEntry import FightResultListEntry
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultFighterListEntry(FightResultListEntry):
    id:int
    alive:bool
    

    def init(self, id:int, alive:bool, outcome:int, wave:int, rewards:'FightLoot'):
        self.id = id
        self.alive = alive
        
        super().__init__(outcome, wave, rewards)
    
    