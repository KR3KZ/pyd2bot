from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    from com.ankamagames.dofus.network.types.game.context.fight.FightLoot import FightLoot
    


class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
    level:int
    guildInfo:'BasicGuildInformations'
    experienceForGuild:int
    

    def init(self, level:int, guildInfo:'BasicGuildInformations', experienceForGuild:int, id:int, alive:bool, outcome:int, wave:int, rewards:'FightLoot'):
        self.level = level
        self.guildInfo = guildInfo
        self.experienceForGuild = experienceForGuild
        
        super().__init__(id, alive, outcome, wave, rewards)
    
    