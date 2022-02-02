from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.AllianceFactSheetInformations import AllianceFactSheetInformations
from com.ankamagames.dofus.network.types.game.social.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
from com.ankamagames.dofus.network.types.game.prism.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo


@dataclass
class AllianceInsiderInfoMessage(NetworkMessage):
    allianceInfos:AllianceFactSheetInformations
    guilds:list[GuildInsiderFactSheetInformations]
    prisms:list[PrismSubareaEmptyInfo]
    
    
    def __post_init__(self):
        super().__init__()
    