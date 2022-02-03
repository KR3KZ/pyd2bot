from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class GuildCreationValidMessage(NetworkMessage):
    guildName:str
    guildEmblem:'GuildEmblem'
    

    def init(self, guildName:str, guildEmblem:'GuildEmblem'):
        self.guildName = guildName
        self.guildEmblem = guildEmblem
        
        super().__init__()
    
    