from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class GuildApplicationIsAnsweredMessage(NetworkMessage):
    accepted:bool
    guildInformation:'GuildInformations'
    

    def init(self, accepted:bool, guildInformation:'GuildInformations'):
        self.accepted = accepted
        self.guildInformation = guildInformation
        
        super().__init__()
    
    