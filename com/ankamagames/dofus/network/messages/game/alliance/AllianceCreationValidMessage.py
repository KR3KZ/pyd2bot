from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceCreationValidMessage(NetworkMessage):
    allianceName:str
    allianceTag:str
    allianceEmblem:'GuildEmblem'
    

    def init(self, allianceName:str, allianceTag:str, allianceEmblem:'GuildEmblem'):
        self.allianceName = allianceName
        self.allianceTag = allianceTag
        self.allianceEmblem = allianceEmblem
        
        super().__init__()
    
    