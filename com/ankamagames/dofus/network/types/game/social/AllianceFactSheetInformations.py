from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceFactSheetInformations(AllianceInformations):
    creationDate:int
    

    def init(self, creationDate:int, allianceEmblem:'GuildEmblem', allianceName:str, allianceId:int, allianceTag:str):
        self.creationDate = creationDate
        
        super().__init__(allianceEmblem, allianceName, allianceId, allianceTag)
    
    