from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
    from com.ankamagames.dofus.network.types.game.social.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
    from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
    


class AllianceInsiderInfoMessage(NetworkMessage):
    allianceInfos:'AllianceFactSheetInformations'
    guilds:list['GuildInsiderFactSheetInformations']
    prisms:list['PrismSubareaEmptyInfo']
    

    def init(self, allianceInfos:'AllianceFactSheetInformations', guilds:list['GuildInsiderFactSheetInformations'], prisms:list['PrismSubareaEmptyInfo']):
        self.allianceInfos = allianceInfos
        self.guilds = guilds
        self.prisms = prisms
        
        super().__init__()
    
    