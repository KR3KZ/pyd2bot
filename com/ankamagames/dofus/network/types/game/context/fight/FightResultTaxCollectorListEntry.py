from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
    level:int
    guildInfo:BasicGuildInformations
    experienceForGuild:int
    
    
