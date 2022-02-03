from com.ankamagames.dofus.network.messages.game.guild.tax.GuildFightJoinRequestMessage import GuildFightJoinRequestMessage


class GuildFightTakePlaceRequestMessage(GuildFightJoinRequestMessage):
    replacedCharacterId:int
    

    def init(self, replacedCharacterId:int, taxCollectorId:int):
        self.replacedCharacterId = replacedCharacterId
        
        super().__init__(taxCollectorId)
    
    