from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.GuildEmblem import GuildEmblem
    


class AllianceFactSheetInformations(AllianceInformations):
    creationDate:int
    

    def init(self, creationDate_:int, allianceEmblem_:'GuildEmblem', allianceName_:str, allianceId_:int, allianceTag_:str):
        self.creationDate = creationDate_
        
        super().__init__(allianceEmblem_, allianceName_, allianceId_, allianceTag_)
    
    