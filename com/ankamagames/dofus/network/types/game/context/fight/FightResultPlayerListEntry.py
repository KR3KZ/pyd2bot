from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultPlayerListEntry(FightResultFighterListEntry):
    level:int
    additional:list['FightResultAdditionalData']
    

    def init(self, level:int, additional:list['FightResultAdditionalData'], id:int, alive:bool, outcome:int, wave:int, rewards:'FightLoot'):
        self.level = level
        self.additional = additional
        
        super().__init__(id, alive, outcome, wave, rewards)
    
    