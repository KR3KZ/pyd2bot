from com.ankamagames.dofus.network.types.game.context.fight.AbstractFightTeamInformations import AbstractFightTeamInformations


class FightTeamLightInformations(AbstractFightTeamInformations):
    teamMembersCount:int
    meanLevel:int
    hasFriend:bool
    hasGuildMember:bool
    hasAllianceMember:bool
    hasGroupMember:bool
    hasMyTaxCollector:bool
    

    def init(self, teamMembersCount:int, meanLevel:int, teamId:int, leaderId:int, teamSide:int, teamTypeId:int, nbWaves:int):
        self.teamMembersCount = teamMembersCount
        self.meanLevel = meanLevel
        
        super().__init__(teamId, leaderId, teamSide, teamTypeId, nbWaves)
    
    