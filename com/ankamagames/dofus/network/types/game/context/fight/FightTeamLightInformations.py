from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations


class FightTeamLightInformations(AbstractFightTeamInformations):
    protocolId = 68
    teamMembersCount:int
    meanLevel:int
    hasFriend:bool
    hasGuildMember:bool
    hasAllianceMember:bool
    hasGroupMember:bool
    hasMyTaxCollector:bool
    
    
