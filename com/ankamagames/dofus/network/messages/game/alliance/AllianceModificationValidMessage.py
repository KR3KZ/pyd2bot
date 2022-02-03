from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceModificationValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    Alliancemblem:'GuildEmblem'
    

    def init(self, allianceName:str, allianceTag:str, Alliancemblem:'GuildEmblem'):
        self.allianceName = allianceName
        self.allianceTag = allianceTag
        self.Alliancemblem = Alliancemblem
        
        super().__init__()
    
    