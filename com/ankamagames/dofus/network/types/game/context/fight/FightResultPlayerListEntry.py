from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from com.ankamagames.dofus.network.types.game.context.fight.FightResultAdditionalData import FightResultAdditionalData


class FightResultPlayerListEntry(FightResultFighterListEntry):
    level:int
    additional:list[FightResultAdditionalData]
    
    
