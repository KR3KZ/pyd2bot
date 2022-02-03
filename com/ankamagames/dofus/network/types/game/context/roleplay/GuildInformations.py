from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildInformations(BasicGuildInformations):
    guildEmblem:'GuildEmblem'
    

    def init(self, guildEmblem:'GuildEmblem', guildId:int, guildName:str, guildLevel:int):
        self.guildEmblem = guildEmblem
        
        super().__init__(guildId, guildName, guildLevel)
    
    