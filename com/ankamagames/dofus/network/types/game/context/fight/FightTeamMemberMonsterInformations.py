from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberMonsterInformations(FightTeamMemberInformations):
    protocolId = 6386
    monsterId:int
    grade:int
    
    
