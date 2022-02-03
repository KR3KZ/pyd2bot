from com.ankamagames.dofus.network.types.game.context.roleplay.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceInformations(BasicNamedAllianceInformations):
    allianceEmblem:'GuildEmblem'
    

    def init(self, allianceEmblem:'GuildEmblem', allianceName:str, allianceId:int, allianceTag:str):
        self.allianceEmblem = allianceEmblem
        
        super().__init__(allianceName, allianceId, allianceTag)
    
    