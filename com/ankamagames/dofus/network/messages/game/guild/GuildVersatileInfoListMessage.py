from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.GuildVersatileInformations import GuildVersatileInformations
    


class GuildVersatileInfoListMessage(NetworkMessage):
    guilds:list['GuildVersatileInformations']
    

    def init(self, guilds:list['GuildVersatileInformations']):
        self.guilds = guilds
        
        super().__init__()
    
    