from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember
    


class GuildInformationsMemberUpdateMessage(NetworkMessage):
    member:'GuildMember'
    

    def init(self, member:'GuildMember'):
        self.member = member
        
        super().__init__()
    
    