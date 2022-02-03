from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildInAllianceInformations(GuildInformations):
    nbMembers:int
    joinDate:int
    

    def init(self, nbMembers:int, joinDate:int, guildEmblem:'GuildEmblem', guildId:int, guildName:str, guildLevel:int):
        self.nbMembers = nbMembers
        self.joinDate = joinDate
        
        super().__init__(guildEmblem, guildId, guildName, guildLevel)
    
    