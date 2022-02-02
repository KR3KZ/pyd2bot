from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


@dataclass
class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
    level:int
    guildInfo:BasicGuildInformations
    experienceForGuild:int
    
    
    def __post_init__(self):
        super().__init__()
    