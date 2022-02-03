from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class HumanOptionGuild(HumanOption):
    guildInformations:'GuildInformations'
    

    def init(self, guildInformations:'GuildInformations'):
        self.guildInformations = guildInformations
        
        super().__init__()
    
    