from com.ankamagames.dofus.network.types.game.context.fight.FightResultFighterListEntry import FightResultFighterListEntry
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
    protocolId = 1517
    level:int
    guildInfo:BasicGuildInformations
    experienceForGuild:int
    
    
