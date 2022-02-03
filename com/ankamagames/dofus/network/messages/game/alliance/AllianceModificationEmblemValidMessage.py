from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceModificationEmblemValidMessage(NetworkMessage):
    Alliancemblem:'GuildEmblem'
    

    def init(self, Alliancemblem:'GuildEmblem'):
        self.Alliancemblem = Alliancemblem
        
        super().__init__()
    
    