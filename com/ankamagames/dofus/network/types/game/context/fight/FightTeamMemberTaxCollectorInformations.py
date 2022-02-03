from com.ankamagames.dofus.network.types.game.context.fight.FightTeamMemberInformations import FightTeamMemberInformations


class FightTeamMemberTaxCollectorInformations(FightTeamMemberInformations):
    firstNameId:int
    lastNameId:int
    level:int
    guildId:int
    uid:int
    

    def init(self, firstNameId:int, lastNameId:int, level:int, guildId:int, uid:int, id:int):
        self.firstNameId = firstNameId
        self.lastNameId = lastNameId
        self.level = level
        self.guildId = guildId
        self.uid = uid
        
        super().__init__(id)
    
    