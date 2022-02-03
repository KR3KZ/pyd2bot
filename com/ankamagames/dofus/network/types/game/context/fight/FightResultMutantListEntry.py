from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultMutantListEntry(FightResultFighterListEntry):
    level:int
    

    def init(self, level:int, id:int, alive:bool, outcome:int, wave:int, rewards:'FightLoot'):
        self.level = level
        
        super().__init__(id, alive, outcome, wave, rewards)
    
    