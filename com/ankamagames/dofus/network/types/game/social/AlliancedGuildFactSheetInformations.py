from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AlliancedGuildFactSheetInformations(GuildInformations):
    allianceInfos:'BasicNamedAllianceInformations'
    

    def init(self, allianceInfos:'BasicNamedAllianceInformations', guildEmblem:'GuildEmblem', guildId:int, guildName:str, guildLevel:int):
        self.allianceInfos = allianceInfos
        
        super().__init__(guildEmblem, guildId, guildName, guildLevel)
    
    