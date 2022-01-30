from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberTaxCollectorInformations(FightTeamMemberInformations):
    protocolId = 9850
    firstNameId:int
    lastNameId:int
    level:int
    guildId:int
    uid:int
    
