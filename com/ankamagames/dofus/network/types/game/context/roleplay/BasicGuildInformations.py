from com.ankamagames.dofus.network.types.game.social.AbstractSocialGroupInfos import AbstractSocialGroupInfos


class BasicGuildInformations(AbstractSocialGroupInfos):
    guildId:int
    guildName:str
    guildLevel:int
    

    def init(self, guildId:int, guildName:str, guildLevel:int):
        self.guildId = guildId
        self.guildName = guildName
        self.guildLevel = guildLevel
        
        super().__init__()
    
    